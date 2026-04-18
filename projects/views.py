from django.shortcuts import render
from django.http import HttpResponse
from .models import Project
from django.views import generic
# Create your views here. 

# Views are the functions that will be called when a user visits a specific URL. 
# They are responsible for returning a response to the user, 
# which can be an HTML page, a JSON object, or any other type of data.

class ProjectListView(generic.ListView):
    model = Project
    template_name = 'project_list.html'
    context_Object_name = 'list'

class Detailview(generic.DetailView):
    model = Project
    template_name = 'project_details.html'
    context_object_name = 'details'