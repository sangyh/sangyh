---
author: "Sangy"
title: "Tokenization"
draft: false
date: "2025-07-16"
description: "Language Modeling from Scratch Part-1"
tags: ["llms"]
categories: ["llms"]
series: ["language-modeling-from-scratch"]
aliases: []
cover:
  image: 
  caption: 
---

- Tiktokenizer is a handly website to see how different models tokenize strings.
- Tokenizers
  - Character tokenization
    - inefficient use of vocab as each character is allotted a id
  - Byte-based tokenizer
    - unicode strings can be represented as sequence of bytes (eg- utf-8 encoding).
    - small vocab - only 256, characters can be between represented as sequence of bytes
    - results in long sequences, attention is quadratic with sequence length so will be poor efficiency
  - work tokenizer
    - split sequence to sequence of strings and assign to an index in vocab
    - no fixed vocab size, unbounded. 
    - might encounter UNK with new tokens
  - Byte-pair encoding (BPE)
    - basic- train tokenizer on raw text to automatically determine the vocabulary
    - intuition - common sequences of characters represented by single token, rare sequences represetned by many tokens
    - Algorithm - start with each byte as token, and successively merge most common pair of adjacent tokens


BPE Algorithm

```
def train_bpe(string: str, num_merges: int) -> BPETokenizerParams:
    Start with the list of bytes of string.
    indices = list(map(int, string.encode("utf-8"))) 
    merges: dict[tuple[int, int], int] = {}  # index1, index2 => merged index
    vocab: dict[int, bytes] = {x: bytes([x]) for x in range(256)}  # index -> bytes
    
    for i in range(num_merges):
        Count the number of occurrences of each pair of tokens
        counts = defaultdict(int)
        for index1, index2 in zip(indices, indices[1:]):  # For each adjacent pair
            counts[(index1, index2)] += 1  # @inspect counts
        
        Find the most common pair.
        pair = max(counts, key=counts.get)  # @inspect pair
        index1, index2 = pair
        
        Merge that pair.
        new_index = 256 + i  # @inspect new_index
        merges[pair] = new_index  # @inspect merges
        vocab[new_index] = vocab[index1] + vocab[index2]  # @inspect vocab
        indices = merge(indices, pair, new_index)  # @inspect indices
    
    return BPETokenizerParams(vocab=vocab, merges=merges)

```
