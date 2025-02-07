#!/usr/bin/env python3

import sys
from pathlib import Path
import re
from typing import List, Dict, Tuple
from dataclasses import dataclass
import yaml
from difflib import SequenceMatcher

@dataclass
class SearchResult:
    file: Path
    title: str
    snippet: str
    score: float
    match_type: str

class EnhancedSearch:
    def __init__(self, notes_dir: Path = Path("notes")):
        self.notes_dir = notes_dir
        self.note_cache: Dict[Path, Dict] = {}
        self._build_cache()

    def _build_cache(self):
        """Build a cache of all notes with their metadata."""
        for file in self.notes_dir.rglob("*.md"):
            content = file.read_text()
            try:
                # Extract YAML frontmatter
                if content.startswith("---"):
                    _, frontmatter, body = content.split("---", 2)
                    metadata = yaml.safe_load(frontmatter)
                else:
                    metadata = {}
                    body = content
                
                self.note_cache[file] = {
                    "metadata": metadata,
                    "content": body.strip(),
                    "title": metadata.get("title", file.stem)
                }
            except Exception:
                # If parsing fails, store basic info
                self.note_cache[file] = {
                    "metadata": {},
                    "content": content,
                    "title": file.stem
                }

    def exact_search(self, query: str) -> List[SearchResult]:
        """Perform exact text matching."""
        results = []
        for file, data in self.note_cache.items():
            content = data["content"].lower()
            query_lower = query.lower()
            if query_lower in content:
                # Find the matching context
                start = max(0, content.find(query_lower) - 40)
                end = min(len(content), content.find(query_lower) + len(query) + 40)
                snippet = f"...{content[start:end]}..."
                
                results.append(SearchResult(
                    file=file,
                    title=data["title"],
                    snippet=snippet,
                    score=1.0,
                    match_type="exact"
                ))
        return results

    def fuzzy_search(self, query: str) -> List[SearchResult]:
        """Perform fuzzy text matching."""
        results = []
        for file, data in self.note_cache.items():
            content = data["content"]
            # Calculate fuzzy match score
            score = SequenceMatcher(None, query.lower(), content.lower()).ratio()
            
            if score > 0.3:  # Threshold for fuzzy matches
                # Find best matching section for snippet
                words = content.split()
                best_window = max(
                    [" ".join(words[i:i+10]) for i in range(len(words)-9)],
                    key=lambda x: SequenceMatcher(None, query.lower(), x.lower()).ratio()
                )
                
                results.append(SearchResult(
                    file=file,
                    title=data["title"],
                    snippet=f"...{best_window}...",
                    score=score,
                    match_type="fuzzy"
                ))
        return results

    def search(self, query: str, mode: str = "all") -> List[SearchResult]:
        """Perform search using specified mode(s)."""
        results = []
        
        if mode in ["all", "exact"]:
            results.extend(self.exact_search(query))
        
        if mode in ["all", "fuzzy"]:
            fuzzy_results = self.fuzzy_search(query)
            # Only add fuzzy results for files that don't have exact matches
            existing_files = {r.file for r in results}
            results.extend([r for r in fuzzy_results if r.file not in existing_files])
        
        # Sort by score
        results.sort(key=lambda x: x.score, reverse=True)
        return results

def main():
    if len(sys.argv) < 2:
        print("Usage: enhanced_search.py <query> [mode]")
        print("Modes: all, exact, fuzzy")
        sys.exit(1)

    query = sys.argv[1]
    mode = sys.argv[2] if len(sys.argv) > 2 else "all"

    searcher = EnhancedSearch()
    results = searcher.search(query, mode)

    print(f"\nSearch results for '{query}' (mode: {mode}):\n")
    for i, result in enumerate(results, 1):
        print(f"{i}. {result.title} ({result.match_type}, score: {result.score:.2f})")
        print(f"   File: {result.file}")
        print(f"   {result.snippet}\n")

if __name__ == "__main__":
    main()
