from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from utils.extractor import extract_text
from utils.cleaner import clean_text, extract_skills
import os

def screen_resumes(job_description, resume_files):
    jd_clean = clean_text(job_description)
    jd_skills = extract_skills(job_description)

    results = []

    for file_path in resume_files:
        raw = extract_text(file_path)
        cleaned = clean_text(raw)

        # TF-IDF similarity
        vectorizer = TfidfVectorizer()
        vectors = vectorizer.fit_transform([jd_clean, cleaned])
        score = cosine_similarity(vectors[0], vectors[1])[0][0]
        score_pct = round(score * 100, 1)

        # Skill matching
        resume_skills = extract_skills(raw)
        matched = [s for s in jd_skills if s in resume_skills]

        results.append({
            "name": os.path.basename(file_path),
            "score": score_pct,
            "matched_skills": matched,
            "total_matched": len(matched)
        })

    results.sort(key=lambda x: x["score"], reverse=True)
    return results