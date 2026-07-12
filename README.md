# 🎯 Dynamic Resume-to-JD Fit & Skill Gap Analyzer

An interactive NLP-powered web application that analyzes job seekers' resumes against target Job Descriptions (JDs) to extract skill coverage, compute contextual match scores, and highlight missing technical skill gaps.

🚀 **Live Demo:** [resume-jd-analyzer-01.streamlit.app](https://resume-jd-analyzer-01.streamlit.app/)

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)
![scikit-learn](https://img.shields.io/badge/scikit--learn-NLP-orange.svg)

---

## 📌 Business & Technical Overview

* **The Problem:** Job seekers struggle to understand why their resumes fail automated applicant tracking systems (ATS), while recruiters spend excessive time manually cross-referencing resumes against dense technical requirements.
* **The Solution:** A Streamlit dashboard that parses PDF resumes, cleans text inputs, computes vector similarity scores using **TF-IDF & Cosine Similarity**, and generates a side-by-side skill matrix comparing matched keywords against missing skill gaps.

---

## ✨ Features

* **📄 PDF Parsing:** Automates text extraction from uploaded resume files using `pdfplumber`.
* **📊 Match Engine:** Leverages `scikit-learn` TF-IDF Vectorization and Cosine Similarity to score overall resume-to-JD alignment.
* **🔍 Skill Gap Taxonomy:** Cross-references resume and JD text against a curated technical skill taxonomy (SQL, Python, Power BI, Tableau, dbt, BigQuery, Docker, PyTorch, etc.) to pinpoint missing keywords.
* **🎨 Side-by-Side BA Matrix:** Displays an intuitive breakdown of matched skills vs. missing critical gaps to help applicants tailor their applications.

---

## 🛠️ Tech Stack & Libraries

* **Frontend / Dashboard:** [Streamlit](https://streamlit.io/)
* **NLP & Analytics Engine:** `scikit-learn` (TF-IDF Vectorizer, Cosine Similarity)
* **PDF Processing:** `pdfplumber`
* **Text Normalization:** Python `re` (Regular Expressions)

---

## 🚀 Local Installation & Setup

1. **Clone the Repository:**
   ```bash
   git clone [https://github.com/Shuvangi2004/resume-jd-skill-gap-analyzer.git](https://github.com/Shuvangi2004/resume-jd-skill-gap-analyzer.git)
   cd resume-jd-skill-gap-analyzer
