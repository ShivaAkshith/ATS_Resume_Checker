# matcher/services/skill_matcher.py

SKILLS = [
    "python",
    "java",
    "django",
    "flask",
    "sql",
    "mysql",
    "postgresql",
    "machine learning",
    "deep learning",
    "data analysis",
    "data science",
    "tensorflow",
    "keras",
    "numpy",
    "pandas",
    "scikit learn",
    "rest api",
    "git",
    "github",
    "docker",
    "aws"
]

def extract_skills(text):
    text = text.lower()
    found_skills = []

    for skill in SKILLS:
        if skill in text:
            found_skills.append(skill)

    return list(set(found_skills))
