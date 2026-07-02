from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

def get_score(jd, resume):

    jd_vector = model.encode(jd)

    resume_vector = model.encode(resume)

    score = cosine_similarity(
        [jd_vector],
        [resume_vector]
    )[0][0]

    return score