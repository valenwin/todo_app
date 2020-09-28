import django.views.generic as views
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy

from .forms import ProjectForm, ProjectUpdateForm
from .forms import TaskForm
from .models import Project, Task


class ProjectListView(LoginRequiredMixin,
                      views.ListView):
    model = Project
    template_name = 'base.html'

    def get_context_data(self, **kwargs):
        """With pagination for posts list view"""
        context = super(ProjectListView, self).get_context_data(**kwargs)
        projects = Project.objects.filter(owner=self.request.user)
        context['form'] = ProjectForm()
        context['projects'] = projects
        return context

    def post(self, request, *args, **kwargs):
        try:
            form = ProjectForm(request.POST)
            form.instance.owner = self.request.user
            form.save()
            return redirect('core:todo')
        except ValueError:
            messages.error(request,
                           'The project is already exist.')
            return redirect('core:todo')


class ProjectDetailView(views.DetailView,
                        views.UpdateView):
    model = Project
    form_class = ProjectUpdateForm
    template_name = 'project_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        project = get_object_or_404(self.model,
                                    slug=self.kwargs.get('slug'))
        context['tasks'] = project.tasks.all()
        return context


class ProjectDeleteView(views.DeleteView):
    model = Project
    template_name = 'project_delete.html'
    success_url = reverse_lazy('core:todo')


class TaskCreateView(views.CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'task_create.html'
    success_url = reverse_lazy('core:todo')

    def post(self, request, *args, **kwargs):
        try:
            form = TaskForm(request.POST)
            form.instance.project = Project.objects.get(slug=self.kwargs.get('slug'))
            form.save()
            return redirect('core:project_detail',
                            slug=self.kwargs.get('slug'))
        except ValueError:
            return redirect('core:todo')
