from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from tasks.models import Task

# Create your views here.


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    template_name = "new.html"
    fields = ["name", "start_date", "due_date", "project", "assignee"]

    def get_success_url(self) -> str:
        return reverse_lazy("show_project", args={self.object.project.id})
