from django.contrib import admin
from .models import MatchResult

@admin.register(MatchResult)
class MatchResultAdmin(admin.ModelAdmin):
    list_display = ('id', 'resume', 'job', 'score', 'created_at')
    list_filter = ('job',)