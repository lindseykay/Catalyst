from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from projects.models import Project

# Create your views here.


class ProjectListView(LoginRequiredMixin, ListView):
    model = Project
    template_name = "projects/list.html"
    # context name is "project_list"

    def get_queryset(self):
        return Project.objects.filter(members=self.request.user)


class ProjectDetailView(LoginRequiredMixin, DetailView):
    model = Project
    template_name = "projects/detail.html"

    # context name is "project"


class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    template_name = "projects/new.html"
    fields = ["name", "description", "members"]

    def get_success_url(self) -> str:
        return reverse_lazy("show_project", args=[self.object.id])
