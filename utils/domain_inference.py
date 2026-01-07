from sentence_transformers import SentenceTransformer, util
from data.career_domains import CAREER_DOMAINS

model = SentenceTransformer("all-MiniLM-L6-v2")

def infer_career_domain(resume_text):
    resume_embedding = model.encode(resume_text, convert_to_tensor=True)

    domain_names = list(CAREER_DOMAINS.keys())
    domain_texts = list(CAREER_DOMAINS.values())

    domain_embeddings = model.encode(domain_texts, convert_to_tensor=True)

    similarities = util.cos_sim(resume_embedding, domain_embeddings)[0]

    best_index = similarities.argmax().item()
    best_domain = domain_names[best_index]
    confidence = round(float(similarities[best_index]) * 100, 2)

    return best_domain, confidence
