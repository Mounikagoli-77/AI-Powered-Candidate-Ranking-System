SKILLS = [
    "Python",
    "Machine Learning",
    "Deep Learning",
    "NLP",
    "SQL",
    "FastAPI",
    "Flask",
    "Django",
    "TensorFlow",
    "PyTorch",
    "Java",
    "React",
    "Node.js",
    "MongoDB",
    "Data Analysis"
]

def extract_skills(text):

    found = []

    for skill in SKILLS:

        if skill.lower() in text.lower():
            found.append(skill)

    return found