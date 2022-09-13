from django.shortcuts import render
from django.views.generic.list import ListView

from projects.models import Project

# Create your views here.


class ProjectListView(ListView):
    model = Project
    template_name = "list.html"
    # context name is "project_list"
