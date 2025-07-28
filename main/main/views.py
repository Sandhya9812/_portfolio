from django.shortcuts import render
from project.models import Project  # ✅ from your project app
from certificates.models import Certificate  # ✅ from your certificates app

# Home page
def home(request):
    return render(request, 'home.html')

# About page
def about(request):
    return render(request, 'about.html')

# Skills page
def skills(request):
    return render(request, 'skills.html')

# Internships page (static unless dynamic model is needed)
def internships(request):
    return render(request, 'internship.html')

# Project showcase page
def projects(request):
    projects = Project.objects.all()
    return render(request, 'project.html', {'projects': projects})

# Certificates page
def certificates(request):
    certificates = Certificate.objects.all()
    return render(request, 'certificates.html', {'certificates': certificates})

def ai_page(request):
    return render(request, 'ai_assistant.html')

