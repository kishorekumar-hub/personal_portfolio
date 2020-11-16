from django.shortcuts import render
from .models import Project,Experience

def home(request):
    projects = Project.objects.all()
    experience = Experience.objects.all()
    return render(request,'portfolio/home.html',{'projects':projects, 'experience':experience})
