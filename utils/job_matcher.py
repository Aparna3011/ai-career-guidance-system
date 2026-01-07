from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from data.job_roles import JOB_ROLES

def match_job_role(resume_text):
    documents = [resume_text] + list(JOB_ROLES.values())
    role_names = list(JOB_ROLES.keys())

    vectorizer = TfidfVectorizer(stop_words="english")
    tfidf_matrix = vectorizer.fit_transform(documents)

    similarity_scores = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:])[0]

    best_match_index = similarity_scores.argmax()
    best_role = role_names[best_match_index]
    best_score = similarity_scores[best_match_index]

    return best_role, round(best_score * 100, 2)
