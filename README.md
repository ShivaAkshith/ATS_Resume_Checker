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

---

🧪 How to Use the App
Paste the Job Description / Required Skills
Upload a resume PDF
Click Check Resume Match
View result:
GOOD MATCH / NOT A GOOD MATCH
Matched skills
Missing skills

