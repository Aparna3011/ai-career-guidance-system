from utils.skill_extractor import extract_skills
from utils.job_matcher import match_job_role

import streamlit as st
import PyPDF2

def extract_text_from_pdf(pdf_file):
    text = ""
    reader = PyPDF2.PdfReader(pdf_file)
    for page in reader.pages:
        text += page.extract_text()
    return text

st.set_page_config(page_title="AI Career Guidance", layout="centered")

st.title("AI Career Guidance System")
st.write("Upload your resume as a PDF or paste the text manually.")

option = st.radio(
    "Choose resume input method:",
    ("Paste Resume Text", "Upload Resume PDF")
)

resume_text = ""

if option == "Paste Resume Text":
    resume_text = st.text_area("Paste resume text here", height=300)

elif option == "Upload Resume PDF":
    file = st.file_uploader("Upload PDF resume", type=["pdf"])
    if file:
        resume_text = extract_text_from_pdf(file)
        st.success("Resume text extracted successfully")

if resume_text:
    st.subheader("Extracted Resume Text")
    st.text(resume_text[:1500])

if resume_text:
    skills = extract_skills(resume_text)

    st.subheader("Detected Skills")
    if skills:
        st.success(", ".join(skills))
    else:
        st.warning("No skills detected. Try updating resume text.")


if resume_text:
    role, score = match_job_role(resume_text)

    st.subheader("Recommended Job Role")
    st.info(f"{role} (Match Score: {score}%)")


