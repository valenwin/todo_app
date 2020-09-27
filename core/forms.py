from django import forms
from django.core.exceptions import ValidationError

from .models import Project


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
