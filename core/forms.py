from django import forms
from django.core.exceptions import ValidationError

from .models import Project, Task


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('title', 'description')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control',
                                            'placeholder': 'Project Name'}),
            'description': forms.Textarea(attrs={'class': 'form-control',
                                                 'placeholder': 'Description',
                                                 'rows': 5}),
        }

    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()
        if new_slug == 'create':
            raise ValidationError('Slug may not be "Create"')
        return new_slug


class ProjectUpdateForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('title',)

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control',
                                            'placeholder': 'Rename Your Project'}),
        }


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'priority', 'due_date', 'complete')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control new-task',
                                            'placeholder': 'Task Name'}),
            'complete': forms.CheckboxInput(attrs={'class': 'form-control new-task'}),
            'priority': forms.Select(attrs={'class': 'form-control new-task',
                                            'placeholder': 'Priority'}),
            'due_date': forms.DateTimeInput(attrs={'class': 'form-control new-task'}),
        }
