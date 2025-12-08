from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    tools = models.CharField(max_length=200, blank=True)  # e.g. Power BI, SQL, Excel
    project_image = models.ImageField(upload_to='projects/', blank=True, null=True)
    live_link = models.URLField(blank=True, null=True)  # e.g. Power BI dashboard URL
    github_link = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
