# forms.py
from django import forms
from .models import Project

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'tools', 'project_image', 'live_link', 'github_link']
        widgets = {
            'description': forms.Textarea(attrs={'rows':4}),
        }
