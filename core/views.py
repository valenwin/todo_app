import django.views.generic as views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect

from .forms import ProjectForm
from .models import Project


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


class ProjectDetailView(views.DetailView):
    model = Project
    template_name = 'project_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        project = get_object_or_404(self.model, slug=self.kwargs.get('slug'))
        context['tasks'] = project.tasks.all()
        return context
