# ATS Resume Checker 🧠📄

A Django-based web application that checks whether a **resume is a good match for a given Job Description (JD)**, similar to how an **Applicant Tracking System (ATS)** works.

The user pastes a JD, uploads a resume (PDF), and the system evaluates whether the resume is suitable based on **skill matching**.

---

## 🚀 Features

- Upload resume in **PDF format**
- Paste **Job Description / Required Skills**
- Extract text from resume
- Match resume skills with JD skills
- Decide:
  - ✅ GOOD MATCH  
  - ❌ NOT A GOOD MATCH
- Show:
  - Matched skills
  - Missing skills
- Clean & user-friendly UI
- Ready for deployment with a public URL

---

## 🛠️ Tech Stack

- **Backend:** Django (Python)
- **NLP:** NLTK
- **PDF Parsing:** PyPDF2
- **Skill Matching:** Keyword-based logic
- **Frontend:** HTML, Bootstrap
- **Version Control:** Git & GitHub
- **Deployment:** Render

---

## 📂 Project Structure

ATS_Resume_Checker/
│
├── ats_project/                 # Main Django project folder
│   ├── __init__.py
│   ├── settings.py              # Django settings
│   ├── urls.py                  # Project-level URLs
│   ├── wsgi.py                  # WSGI config for deployment
│   └── asgi.py
│
├── resumes/                     # App handling resume uploads
│   ├── migrations/
│   ├── models.py                # Resume model
│   ├── views.py                 # Upload & processing logic
│   ├── urls.py                  # App URLs
│   └── admin.py
│
├── matcher/                     # ATS matching & NLP logic
│   ├── services/
│   │   ├── pdf_parser.py        # Extract text from PDF resumes
│   │   ├── text_cleaner.py      # Text preprocessing
│   │   ├── skill_matcher.py     # Skill extraction & matching
│   │   └── similarity.py        # (Optional) semantic similarity
│   └── __init__.py
│
├── templates/                   # HTML templates
│   ├── base.html
│   ├── upload.html              # JD + Resume upload page
│   └── result.html              # Match result page
│
├── static/                      # Static files (CSS, JS if any)
│
├── build.sh                     # Render build script
├── requirements.txt             # Python dependencies
├── .gitignore                   # Ignored files & folders
├── README.md                    # Project documentation
└── manage.py                    # Django management script

---
📦 Installation
Requirements

- python ≥ 3.10
- pip
- git


