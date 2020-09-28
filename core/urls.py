from django.urls import path
import core.views as views


urlpatterns = [
    path('', views.ProjectListView.as_view(), name='todo'),
    path('<str:slug>/', views.ProjectDetailView.as_view(), name='project_detail'),
    path('<str:slug>/delete/', views.ProjectDeleteView.as_view(), name='project_delete'),
    path('<str:slug>/task/create/', views.TaskCreateView.as_view(), name='create_task'),
    path('task/<str:slug>/update/', views.TaskUpdateView.as_view(), name='update_task'),
    path('task/<str:slug>/delete/', views.TaskDeleteView.as_view(), name='delete_task'),

]
