# matcher.py
from embedder import get_embedding, cosine_similarity

def match(job_text, resume_text):
    job_vec = get_embedding(job_text)
    resume_vec = get_embedding(resume_text)
    score = cosine_similarity(job_vec, resume_vec)
    return round(score * 100, 2)
