from django.contrib import admin

from .models import Project, Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'priority', 'due_date', 'created',)
    list_filter = ('priority', 'created', 'project')
    list_editable = ('priority',)
    search_fields = ('title',)
    ordering = ('due_date',)
    list_per_page = 20


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'created')
    list_filter = ('created', 'updated')
    search_fields = ('owner', 'title', 'description')
    raw_id_fields = ('owner',)
    list_per_page = 20
