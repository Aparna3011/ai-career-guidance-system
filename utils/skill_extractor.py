import re

SKILLS = [
    "python", "java", "c", "c++", "javascript",
    "html", "css", "react", "node",
    "sql", "mysql", "mongodb",
    "machine learning", "data analysis",
    "ai", "deep learning",
    "git", "github",
    "docker", "linux",
    "communication", "problem solving", "teamwork"
]

def extract_skills(text):
    text = text.lower()
    found_skills = []

    for skill in SKILLS:
        pattern = r"\b" + re.escape(skill) + r"\b"
        if re.search(pattern, text):
            found_skills.append(skill)

    return list(set(found_skills))
