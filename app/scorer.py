from sklearn.metrics.pairwise import cosine_similarity

def compute_alignment_score(resume_text: str, jd_text: str, embedder) -> float:
    resume_emb = embedder.encode(resume_text)
    jd_emb = embedder.encode(jd_text)

    similarity = cosine_similarity(
        resume_emb.reshape(1, -1),
        jd_emb.reshape(1, -1)
    )[0][0]

    return float(round(similarity * 100, 2))
