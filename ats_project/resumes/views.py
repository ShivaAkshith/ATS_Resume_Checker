from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Resume

from matcher.services.pdf_parser import extract_text_from_pdf
from matcher.services.text_cleaner import clean_text
from matcher.services.similarity import calculate_similarity
from matcher.services.skill_matcher import extract_skills


@login_required
def upload_resume(request):
    if request.method == 'POST':
        resume_file = request.FILES['resume']
        job_text = request.POST['job_text']

        # Save resume
        resume = Resume.objects.create(
            user=request.user,
            file=resume_file
        )

        # Extract & clean text
        raw_resume_text = extract_text_from_pdf(resume.file)
        cleaned_resume = clean_text(raw_resume_text)
        cleaned_job = clean_text(job_text)

        # Semantic similarity
        similarity_score = calculate_similarity(cleaned_resume, cleaned_job)

        # Skill extraction
        job_skills = extract_skills(cleaned_job)
        resume_skills = extract_skills(cleaned_resume)

        matched = list(set(job_skills) & set(resume_skills))
        missing = list(set(job_skills) - set(resume_skills))

        # Skill score
        # Skill coverage percentage
        if job_skills:
            skill_coverage = (len(matched) / len(job_skills)) * 100
        else:
            skill_coverage = 0

        # Final decision
        if skill_coverage >= 70:
            verdict = "GOOD MATCH"
        else:
            verdict = "NOT A GOOD MATCH"


        return render(request, 'result.html', {
        'verdict': verdict,
        'score': round(skill_coverage, 2),
        'matched': matched,
        'missing': missing,
        'job_text': job_text
        })


    return render(request, 'upload.html')
