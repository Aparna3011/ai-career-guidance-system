import streamlit as st
import PyPDF2

from utils.skill_extractor import extract_skills
from utils.domain_inference import infer_career_domain


# ---------- PDF TEXT EXTRACTION ----------
def extract_text_from_pdf(pdf_file):
    text = ""
    reader = PyPDF2.PdfReader(pdf_file)
    for page in reader.pages:
        extracted = page.extract_text()
        if extracted:
            text += extracted
    return text


# ---------- STREAMLIT CONFIG ----------
st.set_page_config(page_title="AI Career Guidance", layout="centered")

st.title("AI Career Guidance System")
st.write("Upload your resume as a PDF or paste the text manually.")


# ---------- INPUT METHOD ----------
option = st.radio(
    "Choose resume input method:",
    ("Paste Resume Text", "Upload Resume PDF")
)

resume_text = ""


# ---------- TEXT INPUT ----------
if option == "Paste Resume Text":
    resume_text = st.text_area(
        "Paste resume text here",
        height=300
    )


# ---------- PDF INPUT ----------
elif option == "Upload Resume PDF":
    file = st.file_uploader(
        "Upload PDF resume",
        type=["pdf"]
    )
    if file:
        resume_text = extract_text_from_pdf(file)
        st.success("Resume text extracted successfully")


# ---------- PROCESS ONLY IF TEXT EXISTS ----------
if resume_text.strip():

    # Show extracted text
    st.subheader("Extracted Resume Text")
    st.text(resume_text[:1500])

    # ---------- AI CAREER DOMAIN INFERENCE ----------
    domain, confidence = infer_career_domain(resume_text)

    st.subheader("Inferred Career Domain")
    st.info(f"{domain} (Confidence: {confidence}%)")

    # ---------- SKILL EXTRACTION ----------
    skills = extract_skills(resume_text)

    st.subheader("Detected Skills")
    if skills:
        st.success(", ".join(skills))
    else:
        st.warning("No skills detected. Try adding more details to the resume.")
