from django.urls import path
import core.views as views


urlpatterns = [
    path('', views.ProjectListView.as_view(), name='todo'),
    path('<str:slug>/', views.ProjectDetailView.as_view(), name='project_detail'),
    path('<str:slug>/delete/', views.ProjectDeleteView.as_view(), name='project_delete'),

]
