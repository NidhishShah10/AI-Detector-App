# 🤖 AI Detector & Humanizer App

## 📌 Problem Statement
With the rapid advancement of AI writing tools, it has become increasingly difficult to distinguish between human-written and AI-generated content in academic writing. This web app brings together AI detection and natural language processing to detect AI-written essays and rephrase them to sound more human-like. It takes in any essay or piece of text and intelligently rewrites the content while maintaining the original meaning in a more natural and human-like writing style.

This project aims to address these challenges through a full-stack web application.

---

## 🚀 Project Goals
- Build a functional full-stack AI-powered web application
- Provide measurable AI detection results
- Implement meaningful text transformation while preserving semantic content
- Evaluate system performance using real test data

---

## ✍️ Contributors
- Nidhish Shah
- Junfeng Li
- Cole Smolinski
- Stephen Hannawi

---

## 💡 Proposed Method
The system provides two core features:

### 1. AI Detection
- Users paste an essay into the application
- The text is analyzed using the Sapling AI Detection API
- The system returns a score (0–100%) indicating the likelihood that the text is AI-generated

### 2. Humanization (Humanizer)
- The essay is sent to the Groq LLaMA 3.3 70B model
- The essay is rewritten to sound more natural and human-like while preserving the original meaning
- A rewriting analysis shows how much the wording changed compared to the original

---

## 📊 Data Sources
- **Sapling AI API** — AI-generated text detection
- **Groq LLaMA 3.3 70B** — Natural language rephrasing
- **Dataset** — "Human vs AI Generated Essays" by Navjot Kaushal from Kaggle.com

---

## 🛠️ Tech Stack

### Frontend
- HTML, CSS, JavaScript

### Backend
- Python Flask

### APIs & Models
- Sapling AI API — detection
- Groq API — rephrasing (LLaMA 3.3 70B)

### Evaluation
- Scikit-learn — cosine similarity for rewriting analysis
- Pandas — dataset loading and processing
- Custom evaluation script — 99% detection accuracy on 10 sample essays

---

<img width="1392" height="791" alt="image" src="https://github.com/user-attachments/assets/be22c02a-799b-474e-930e-233fec1d7bb4" />


---
