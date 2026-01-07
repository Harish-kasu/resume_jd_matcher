from sklearn.metrics.pairwise import cosine_similarity

SECTION_WEIGHTS = {
    "skills": 0.3,
    "experience": 0.3,
    "projects": 0.2,
    "full_text": 0.2
}

def compute_alignment_score(resume_sections, jd_embedding, embedder) -> float:
    score = 0.0
    weight_sum = 0.0

    for section, weight in SECTION_WEIGHTS.items():
        if section not in resume_sections:
            continue

        section_text = resume_sections[section]
        if not section_text.strip():
            continue

        embedding = embedder.encode(section_text)
        similarity = cosine_similarity(
            embedding.reshape(1, -1),
            jd_embedding.reshape(1, -1)
        )[0][0]

        score += similarity * weight
        weight_sum += weight

    # Absolute safety fallback
    if weight_sum == 0:
        return 0.0

    return  float(round((score / weight_sum) * 100, 2))

