---
author: "Sangy"
title: "Pytorch and Resource Accounting"
draft: false
date: "2025-07-17"
description: "Language Modeling from Scratch Part-2"
tags: [llms,course]
categories: [llms,technical]
series: ["language-modeling-from-scratch"]
aliases: []
cover:
  image: 
  caption: 
---

Some back-of-the-envelope math for training

**Question: How long would it take to train a 70B parameter model on 15T tokens on 1024 H100s?**
```
total_flops = 6 * 70e9 * 15e12  
assert h100_flop_per_sec == 1979e12 / 2
mfu = 0.5
flops_per_day = h100_flop_per_sec * mfu * 1024 * 60 * 60 * 24 
days = total_flops / flops_per_day  
```

**Question: What's the largest model that can you can train on 8 H100s using AdamW (naively)?**
```
h100_bytes = 80e9  
bytes_per_parameter = 4 + 4 + (4 + 4)  # parameters, gradients, optimizer state  
num_parameters = (h100_bytes * 8) / bytes_per_parameter  
```

Caveat 1: we are naively using float32 for parameters and gradients. We could also use bf16 for parameters and gradients (2 + 2) and keep an extra float32 copy of the parameters (4). This doesn't save memory, but is faster.
Caveat 2: activations are not accounted for (depends on batch size and sequence length).

This is a rough back-of-the-envelope calculation.


