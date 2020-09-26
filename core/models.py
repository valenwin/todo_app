from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Project(models.Model):
    title = models.CharField(max_length=120)
    owner = models.ForeignKey(User,
                              related_name='project_owner',
                              on_delete=models.CASCADE)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return self.title


class Task(models.Model):
    PRIORITY = (
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High')
    )
    title = models.CharField(max_length=120)
    project = models.ForeignKey(Project,
                                on_delete=models.CASCADE,
                                related_name='tasks')
    priority = models.CharField(max_length=10,
                                choices=PRIORITY,
                                default='low')
    due_date = models.DateTimeField(default=timezone.now)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return self.title
