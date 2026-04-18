from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from projects.models import Project

""" def landing(request):
    projects = Project.objects.all().order_by('-created_at')
    context = {
        'projects': projects
    } 
    return render(request, 'core/landing.html', context) """

class landing(generic.ListView):
    model = Project
    context_object_name = 'projects' 
    template_name = "core/landing.html"

class test(generic.ListView):
    model = Project 
    context_object_name= 'projects'
    template_name = 'core/test.html'

def about(request):
    return HttpResponse("This is the about page of the website")

def contact(request):
    return HttpResponse("This is the contact page of the website")

