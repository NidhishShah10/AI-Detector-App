# AI Essay Detector & Humanizer App

## 📌 Problem Statement

With the rapid advancement of AI writing tools, it has become increasingly difficult to distinguish between human-written content and AI generated content in academic writing. This web app that brings together AI detection and natural language processing to detect AI written essays and rephrase them to be more human like. This web app takes in any essay or piece of text and then intelligently rephrases the detected AI written content while maintaining the original meaning but in a more natural and human like writing style.  

This project aims to address these challenges through a full stack web application.

---
## 🚀 Project Goals

- Build a functional full stack AI powered web application
- Provide measurable AI detection results
- Implement meaningful text transformation while preserving semantic content
- Evaluate system performance using real test data
---
## ✍ Contributers

- Nidhish Shah
- Junfeng Li
- Cole Smolinski
- Stephen Hannawi

---

## 💡 Proposed Method

The system provides two core features:

### 1. AI Detection
- Users paste an essay into the application.
- The text is analyzed using the Sapling AI Detection API.
- The system returns a score (0–100%) indicating the likelihood that the text is AI generated.

### 2. Humanization
- If the text is flagged as likely AI generated:
  - It is sent to the Anthropic Claude API.
  - The essay is rewritten to sound more natural and human-like while preserving the original meaning.
- The rewritten version is re-evaluated to verify that the AI detection score has improved.

This creates an iterative workflow:

Detect → Rewrite → Re-detect → Compare results

---

## 📊 Data Sources

This project uses the following data sources:

- Sapling AI API – AI-generated text detection
- Anthropic Claude API – Natural language rephrasing
- Hugging Face Model — For local text rephrasing
- Dataset — "Human vs AI Generated Essays" by Navjot Kaushal from Kaggle.com
---

 ## 🛠️ Tech Stack

### Frontend
 - React.js

### Backend
 - Python Flask
---
