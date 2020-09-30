from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from core.models import Project, Task


class PostViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.test_user = User.objects.create_user(email='test_user@test.com',
                                                 username='test_user',
                                                 password='12345')
        cls.project = Project.objects.create(title='Test Project',
                                             owner=cls.test_user,
                                             description='Test Content Description')
        cls.project.slug = 'test-project-title-3009856'

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 302)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get('/test-project-title-3009856/')
        self.assertEqual(resp.status_code, 301)

    def test_view_uses_correct_project(self):
        resp = self.client.get(reverse('core:todo'))
        self.assertEqual(resp.status_code, 302)

    def test_view_uses_correct_project_delete(self):
        resp = self.client.get('/test-project-title-3009856/delete/')
        self.assertEqual(resp.status_code, 404)


class TaskViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.test_user = User.objects.create_user(email='test_user1@test.com',
                                                 username='test_user1',
                                                 password='12345')
        cls.project = Project.objects.create(title='Test Project',
                                             owner=cls.test_user,
                                             description='Test Content Description')
        cls.task = Task.objects.create(title='Test Task',
                                       priority='high',
                                       project=cls.project)
        cls.project.slug = 'test-project-title-3009857'
        cls.task.slug = 'test-task-title-3009856'

    def test_view_uses_correct_project_delete(self):
        resp = self.client.get('/task/test-task-title-3009856/delete/')
        self.assertEqual(resp.status_code, 404)

    def test_view_uses_correct_project(self):
        resp = self.client.get('/task/test-task-title-3009856/update/')
        self.assertEqual(resp.status_code, 301)
