---
title: "AI Engineering Evals 101"
date: 2025-03-29 02:12:44
type: "timeline"
layout: "timeline"
draft: false
tags: ["llms", "evals"]
---


Look at your data. 

- Create a data annotation interface to add **free-form** notes. this forces you to get close to the data
- Annotate until you feel you're not learning anything new.
- Now ask an LLM to create cateogries and assign each sample to categories (multiclass classification)
- Aggregate and analyze failure modes


Now, with every tweak to the app, prompt engineering, model change etc, run evals to compare and contrast. 