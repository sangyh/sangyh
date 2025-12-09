#!/usr/bin/env python3

import sys
from pathlib import Path
import yt_dlp
from datetime import datetime
import re
from openai import OpenAI
from urllib.parse import urlparse, parse_qs, unquote
import argparse
import json
import os
from dotenv import load_dotenv
import shutil
from deepgram import DeepgramClient, PrerecordedOptions, FileSource

# Load environment variables from .env file
load_dotenv()

# Initialize clients
openai_client = OpenAI(
    api_key=os.getenv('OPENAI_API_KEY')
)
deepgram_client = DeepgramClient(os.getenv('DEEPGRAM_API_KEY'))

def clean_url(url):
    """Clean and normalize YouTube URL."""
    # Remove any escape characters
    url = url.replace('\\', '')
    # Ensure proper encoding
    return unquote(url)

def get_video_id(url):
    """Extract video ID from YouTube URL."""
    url = clean_url(url)
    parsed = urlparse(url)
    if parsed.hostname == 'youtu.be':
        return parsed.path[1:]
    if parsed.hostname in ('www.youtube.com', 'youtube.com'):
        if parsed.path == '/watch':
            query = parse_qs(parsed.query)
            return query.get('v', [None])[0]
    return None

def download_audio(url, output_dir, keep_audio=False):
    """Download audio from YouTube video."""
    url = clean_url(url)
    video_id = get_video_id(url)
    if not video_id:
        raise ValueError("Invalid YouTube URL")

    # Create temp directory for initial download
    temp_dir = Path("temp_audio")
    temp_dir.mkdir(exist_ok=True)

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': str(temp_dir / '%(id)s.%(ext)s'),
        'quiet': True,
        'no_warnings': True
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            title = info.get('title', video_id)
            temp_file = temp_dir / f"{video_id}.mp3"
            
            if keep_audio:
                # Create organized directory structure
                date_dir = output_dir / datetime.now().strftime("%Y-%m")
                date_dir.mkdir(parents=True, exist_ok=True)
                
                # Create final filename with title
                safe_title = re.sub(r'[^\w\s-]', '', title.replace(' ', '-'))
                final_file = date_dir / f"{safe_title}-{video_id}.mp3"
                
                # Move file to final location
                shutil.move(str(temp_file), str(final_file))
                return title, final_file
            
            return title, temp_file
            
    except Exception as e:
        raise RuntimeError(f"Failed to download video: {str(e)}")

def transcribe_audio(audio_file):
    """Transcribe audio file using Deepgram API with speaker diarization."""
    try:
        # Read the audio file
        with open(audio_file, 'rb') as audio:
            buffer_data = audio.read()

        # Configure transcription options
        options = PrerecordedOptions(
            model="nova-2",
            language="en",
            punctuate=True,
            diarize=True,
        )

        # Send to Deepgram
        payload = {"buffer": buffer_data}
        response = deepgram_client.listen.rest.v("1").transcribe_file(payload, options)

        # Extract words with speaker and timing info
        words = response.results.channels[0].alternatives[0].words

        # Group words by speaker into turns
        current_speaker = None
        current_turn = []
        turns = []

        for word in words:
            if current_speaker != word.speaker:
                if current_turn:
                    turns.append({
                        'speaker': current_speaker,
                        'start': current_turn[0].start,
                        'end': current_turn[-1].end,
                        'text': ' '.join(w.word for w in current_turn)
                    })
                current_speaker = word.speaker
                current_turn = [word]
            else:
                current_turn.append(word)

        # Add final turn
        if current_turn:
            turns.append({
                'speaker': current_speaker,
                'start': current_turn[0].start,
                'end': current_turn[-1].end,
                'text': ' '.join(w.word for w in current_turn)
            })

        # Format turns into readable transcript
        transcribed_text = '\n\n'.join(
            f"[Speaker {t['speaker']} at {t['start']:.2f}s - {t['end']:.2f}s]\n{t['text']}"
            for t in turns
        )

        return transcribed_text

    except Exception as e:
        raise RuntimeError(f"Failed to transcribe audio: {str(e)}")

def process_with_gpt(text, mode="summarize"):
    """Process text with GPT for summarization or Q&A."""
    try:
        if mode == "summarize":
            prompt = f"""Please provide a comprehensive summary of the following transcript, 
            organized into key points and main takeaways. The transcript includes multiple speakers,
            so please note any important interactions or discussions:

            {text}"""
        else:  # Q&A mode
            prompt = f"""Please analyze the following transcript and generate:
            1. 5 key questions that this content answers
            2. Their detailed answers based on the content
            3. 3 potential follow-up questions for further exploration
            4. A brief overview of the speaker dynamics and key interactions

            Transcript:
            {text}"""

        response = openai_client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that processes video transcripts with multiple speakers."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        raise RuntimeError(f"Failed to process with GPT: {str(e)}")

def create_note(title, transcript, processed_content, video_url, audio_file, mode="summarize"):
    """Create a formatted note with your blog post structure."""
    timestamp = datetime.now().strftime("%Y-%m-%d")
    
    # Determine categories and tags based on mode
    categories = ["content-summary"] if mode == "summarize" else ["content-qa"]
    tags = ["youtube"]
    
    note = f"""---
author: "Sangy Hanumasagar"
title: "{title}"
draft: false
date: "{timestamp}"
description: "Notes from YouTube video analysis with speaker diarization"
tags: {json.dumps(tags)}
categories: {json.dumps(categories)}
series: []
aliases: []
cover:
  image: 
  caption:
---

## Video Information
- Source: {video_url}
- Date Processed: {timestamp}
- Audio File: {audio_file.name if audio_file else "Not saved"}

## {"Summary" if mode == "summarize" else "Q&A Analysis"}

{processed_content}

## Full Transcript
(Timestamps and speaker identification included)

{transcript}
"""
    return note

def main():
    # Check for API keys
    if not os.getenv('OPENAI_API_KEY'):
        print("Error: OPENAI_API_KEY not found in .env file")
        print("Please create a .env file with your OpenAI API key (see .env.example)")
        sys.exit(1)
    
    if not os.getenv('DEEPGRAM_API_KEY'):
        print("Error: DEEPGRAM_API_KEY not found in .env file")
        print("Please add your Deepgram API key to the .env file")
        sys.exit(1)

    parser = argparse.ArgumentParser(description="Process YouTube videos into notes with speaker diarization")
    parser.add_argument("url", help="YouTube video URL")
    parser.add_argument(
        "--mode",
        choices=["summarize", "qa"],
        default="summarize",
        help="Processing mode: summarize or qa (question-answer)"
    )
    parser.add_argument(
        "--keep-audio",
        action="store_true",
        help="Keep the downloaded audio file"
    )
    parser.add_argument(
        "--audio-dir",
        type=str,
        default="downloads/audio",
        help="Directory to store audio files (when using --keep-audio)"
    )
    args = parser.parse_args()

    # Setup directories
    audio_dir = Path(args.audio_dir) if args.keep_audio else None
    
    audio_file = None
    try:
        # Download and process video
        print("Downloading video audio...")
        title, audio_file = download_audio(args.url, audio_dir, args.keep_audio)
        
        print("Transcribing audio using Deepgram API (with speaker diarization)...")
        transcript = transcribe_audio(audio_file)
        
        print(f"Processing content in {args.mode} mode with GPT-4...")
        processed_content = process_with_gpt(transcript, args.mode)
        
        # Create note
        note_content = create_note(title, transcript, processed_content, args.url, audio_file if args.keep_audio else None, args.mode)
        
        # Save note
        sanitized_title = re.sub(r'[^\w\s-]', '', title.replace(' ', '-'))
        
        # Create notes directory structure
        notes_dir = Path("drafts/youtube")
        notes_dir.mkdir(parents=True, exist_ok=True)
        
        # Save the main note with summary/qa
        output_file = notes_dir / f"{sanitized_title}.md"
        output_file.write_text(note_content)
        
        # Also save the raw transcript separately
        transcript_dir = notes_dir / "transcripts"
        transcript_dir.mkdir(exist_ok=True)
        transcript_file = transcript_dir / f"{sanitized_title}-transcript.md"
        
        # Create a simpler markdown file for just the transcript
        transcript_content = f"""---
title: "{title} - Transcript"
date: "{timestamp}"
type: "transcript"
source_url: "{args.url}"
---

# {title} - Full Transcript

## Video Information
- Source: {args.url}
- Date Processed: {timestamp}
- Audio File: {audio_file.name if audio_file else "Not saved"}

## Transcript
(Timestamps and speaker identification included)

{transcript}
"""
        transcript_file.write_text(transcript_content)
        
        print(f"\nCreated note: {output_file}")
        print(f"Created transcript: {transcript_file}")
        if args.keep_audio:
            print(f"Saved audio: {audio_file}")
        
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)
    finally:
        # Cleanup temp files only if not keeping audio
        if not args.keep_audio and audio_file and audio_file.exists():
            try:
                audio_file.unlink()
            except Exception:
                pass
            
        temp_dir = Path("temp_audio")
        if temp_dir.exists() and not any(temp_dir.iterdir()):
            try:
                temp_dir.rmdir()
            except Exception:
                pass

if __name__ == "__main__":
    main() 