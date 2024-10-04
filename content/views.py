from django.shortcuts import render
from .models import Project, Experience

# Create your views here.
def projects_list(request):

    projects = Project.objects.all()

    return render(request, 'content/projects_list.html', {"projects" : projects }
    )

def experience(request):

    experience = Experience.objects.all()

    return render(request, 'content/experience.html', {"experience" : experience})

def contact(request):

    contact = Contact.objects.all()

    return render(request, 'pages/contact.html', {"contact" : contact})