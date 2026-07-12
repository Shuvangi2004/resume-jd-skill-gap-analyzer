import re
import pdfplumber
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import streamlit as st

# 1. Define Hardcoded Technical Skill Taxonomy
TECH_TAXONOMY = {
    "python",
    "sql",
    "power bi",
    "tableau",
    "dbt",
    "bigquery",
    "excel",
    "git",
    "scikit-learn",
    "pandas",
    "numpy",
    "fastapi",
    "docker",
    "aws",
    "gcp",
    "pytorch",
    "tensorflow",
    "nlp",
    "r",
}


# 2. Text Extraction & Sanitization
def extract_text_from_pdf(pdf_file):
  text = ""
  try:
    with pdfplumber.open(pdf_file) as pdf:
      for page in pdf.pages:
        extracted = page.extract_text()
        if extracted:
          text += extracted + "\n"
  except Exception as e:
    st.error(f"Error reading PDF file: {e}")
  return text


def clean_text(text):
  text = text.lower()
  text = re.sub(r"http\S+\s*", " ", text)
  text = re.sub(r"[^\w\s]", " ", text)
  text = re.sub(r"\s+", " ", text).strip()
  return text


# 3. ML Scoring Engine
def compute_similarity(resume, jd):
  try:
    vectorizer = TfidfVectorizer(stop_words="english")
    tfidf = vectorizer.fit_transform([resume, jd])
    score = cosine_similarity(tfidf[0:1], tfidf[1:2])[0][0]
    return round(score * 100, 2)
  except Exception as e:
    st.error(f"Error calculating similarity: {e}")
    return 0.0


# 4. Skill Extraction & Gap Analysis Logic
def extract_skills(text):
  found = set()
  cleaned = text.lower()
  for skill in TECH_TAXONOMY:
    if re.search(r"\b" + re.escape(skill) + r"\b", cleaned):
      found.add(skill)
  return found


# 5. Streamlit Dashboard Layout
st.set_page_config(
    page_title="Resume-to-JD Skill Gap Analyzer", layout="wide"
)

st.title("🎯 Dynamic Resume-to-JD Fit & Skill Gap Analyzer")
st.caption(
    "Upload your resume PDF and paste a target Job Description to analyze match"
    " percentage and missing technical skill gaps."
)

col1, col2 = st.columns(2)

with col1:
  uploaded_file = st.file_uploader("1. Upload Resume (PDF)", type=["pdf"])

with col2:
  jd_input = st.text_area(
      "2. Paste Job Description (JD)",
      height=180,
      placeholder="Paste job posting text here...",
  )

if st.button("🚀 Analyze Fit & Skill Gaps"):
  if not uploaded_file:
    st.warning("Please upload a PDF resume first!")
  elif not jd_input.strip():
    st.warning("Please paste a Job Description first!")
  else:
    with st.spinner("Analyzing resume against job description..."):
      resume_raw = extract_text_from_pdf(uploaded_file)

      if not resume_raw.strip():
        st.error(
            "Could not extract text from the uploaded PDF. Make sure it is not"
            " an image-only/scanned PDF."
        )
      else:
        resume_clean = clean_text(resume_raw)
        jd_clean = clean_text(jd_input)

        # Run ML Pipeline
        score = compute_similarity(resume_clean, jd_clean)
        resume_skills = extract_skills(resume_clean)
        jd_skills = extract_skills(jd_clean)

        matched_skills = sorted(list(resume_skills.intersection(jd_skills)))
        missing_skills = sorted(list(jd_skills - resume_skills))

        st.markdown("---")
        st.metric(label="Overall Resume Match Score", value=f"{score}%")

        # Side-by-Side BA Matrix
        res_col1, res_col2 = st.columns(2)

        with res_col1:
          st.subheader("✅ Matched Skills")
          if matched_skills:
            for s in matched_skills:
              st.success(f"✓ {s.upper()}")
          else:
            st.info("No matching taxonomy skills detected.")

        with res_col2:
          st.subheader("❌ Missing Skill Gaps")
          if missing_skills:
            for s in missing_skills:
              st.error(f"✗ {s.upper()}")
          else:
            st.balloons()
            st.success("No missing taxonomy skill gaps detected!")