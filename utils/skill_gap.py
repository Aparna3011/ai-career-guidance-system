from data.domain_skills import DOMAIN_SKILLS

def recommend_skill_gap(domain, extracted_skills, max_recommendations=5):
    extracted_skills = [s.lower() for s in extracted_skills]

    if domain not in DOMAIN_SKILLS:
        return []

    domain_required_skills = DOMAIN_SKILLS[domain]

    missing_skills = [
        skill for skill in domain_required_skills
        if skill.lower() not in extracted_skills
    ]

    return missing_skills[:max_recommendations]
