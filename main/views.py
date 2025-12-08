from django.shortcuts import render

# views.py
from django.shortcuts import render, redirect
from .models import Project
from .forms import ProjectForm  # we'll create this next

def home(request):
    projects = Project.objects.order_by('-created_at')  # newest first
    return render(request, 'home.html', {'projects': projects})

def add_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')  # redirect to home to see the new project
    else:
        form = ProjectForm()
    return render(request, 'add_project.html', {'form': form})


def contact(request):
    return render(request, 'contact.html')
