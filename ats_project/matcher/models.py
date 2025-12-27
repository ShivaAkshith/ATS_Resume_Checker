from django.db import models
from resumes.models import Resume
from jobs.models import JobDescription

class MatchResult(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    job = models.ForeignKey(JobDescription, on_delete=models.CASCADE)
    score = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.resume} - {self.job} : {self.score}%"