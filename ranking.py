from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from skills import extract_skills
import re

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

def calculate_score(job_description,
                    resume_text):

    # Semantic Similarity

    job_vector = model.encode(
        job_description
    )

    resume_vector = model.encode(
        resume_text
    )

    semantic_score = cosine_similarity(
        [job_vector],
        [resume_vector]
    )[0][0] * 100

    # Skill Matching

    jd_skills = extract_skills(
        job_description
    )

    resume_skills = extract_skills(
        resume_text
    )

    if len(jd_skills) > 0:

        matched_skills = list(
            set(jd_skills)
            &
            set(resume_skills)
        )

        missing_skills = list(
            set(jd_skills)
            -
            set(resume_skills)
        )

        skill_score = (
            len(matched_skills)
            /
            len(jd_skills)
        ) * 100

    else:

        matched_skills = []
        missing_skills = []
        skill_score = 0

    # Experience Extraction

    match = re.search(
        r'(\d+)\s+years',
        resume_text.lower()
    )

    if match:

        years = int(
            match.group(1)
        )

    else:

        years = 0

    experience_score = min(
        years * 10,
        100
    )

    # Final Score

    final_score = (

        0.4 * semantic_score +

        0.4 * skill_score +

        0.2 * experience_score

    )

    # Recommendation

    if final_score >= 50:

        recommendation = "Strong Hire"

    elif final_score >= 30:

        recommendation = "Consider"

    else:

        recommendation = "Not Recommended"

    return {

        "final_score":
        round(final_score, 2),

        "semantic_score":
        round(semantic_score, 2),

        "skill_score":
        round(skill_score, 2),

        "experience":
        years,

        "matched_skills":
        matched_skills,

        "missing_skills":
        missing_skills,

        "recommendation":
        recommendation
    }