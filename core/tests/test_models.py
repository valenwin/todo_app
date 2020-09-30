import datetime

from django.contrib.auth.models import User
from django.test import TestCase

from core.models import Project, Task


class PostModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.test_user = User.objects.create_user(email='test_user@test.com',
                                                 username='test_user',
                                                 password='12345')
        cls.project = Project.objects.create(title='Test Project',
                                             owner=cls.test_user,
                                             description='Test Content Description')
        cls.project.slug = 'test-project-title-3009856'

    def test_get_absolute_url(self):
        self.assertEquals(self.project.get_absolute_url(),
                          '/test-project-title-3009856/')

    def test_get_delete_url(self):
        self.assertEquals(self.project.get_delete_url(),
                          '/test-project-title-3009856/delete/')

    def test_title_label(self):
        field_label = self.project._meta.get_field('title').verbose_name
        self.assertEquals(field_label, 'title')

    def test_title_max_length(self):
        max_length = self.project._meta.get_field('title').max_length
        self.assertEquals(max_length, 120)

    def test_title_data(self):
        self.assertEquals(self.project.title, 'Test Project')

    def test_description_label(self):
        field_label = self.project._meta.get_field('description').verbose_name
        self.assertEquals(field_label, 'description')

    def test_description_max_length(self):
        max_length = self.project._meta.get_field('description').max_length
        self.assertEquals(max_length, None)

    def test_description_data(self):
        self.assertEquals(self.project.description, 'Test Content Description')

    def test_created_label(self):
        field_label = self.project._meta.get_field('created').verbose_name
        self.assertEquals(field_label, 'created')

    def test_created_date(self):
        date = self.project.created.date().today()
        self.assertEquals(date, datetime.date.today())

    def test_owner_label(self):
        field_label = self.project._meta.get_field('owner').verbose_name
        self.assertEquals(field_label, 'owner')

    def test_owner_data(self):
        self.assertEquals(self.project.owner, self.test_user)

    def test_slug_label(self):
        field_label = self.project._meta.get_field('slug').verbose_name
        self.assertEquals(field_label, 'slug')

    def test_slug_max_length(self):
        max_length = self.project._meta.get_field('slug').max_length
        self.assertEquals(max_length, 250)

    def test_object_title(self):
        expected_object_title = self.project.title
        self.assertEquals(expected_object_title, str(self.project))


class TaskModelTest(TestCase):

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

    def test_get_absolute_url(self):
        self.assertEquals(self.task.get_absolute_url(),
                          '/test-project-title-3009857/')

    def test_get_update_url(self):
        self.assertEquals(self.task.get_update_url(),
                          '/task/test-task-title-3009856/update/')

    def test_get_delete_url(self):
        self.assertEquals(self.task.get_delete_url(),
                          '/task/test-task-title-3009856/delete/')

    def test_title_label(self):
        field_label = self.task._meta.get_field('title').verbose_name
        self.assertEquals(field_label, 'title')

    def test_title_max_length(self):
        max_length = self.task._meta.get_field('title').max_length
        self.assertEquals(max_length, 120)

    def test_title_data(self):
        self.assertEquals(self.task.title, 'Test Task')

    def test_priority_label(self):
        field_label = self.task._meta.get_field('priority').verbose_name
        self.assertEquals(field_label, 'priority')

    def test_priority_max_length(self):
        max_length = self.task._meta.get_field('priority').max_length
        self.assertEquals(max_length, 10)

    def test_priority_data_equal(self):
        self.assertEquals(self.task.priority, 'high')

    def test_priority_data_not_equal(self):
        self.assertNotEquals(self.task.priority, 'low')
        self.assertNotEquals(self.task.priority, 'medium')

    def test_project_label(self):
        field_label = self.task._meta.get_field('project').verbose_name
        self.assertEquals(field_label, 'project')

    def test_project_data(self):
        self.assertEquals(self.task.project, self.project)

    def test_task_project_data_title(self):
        self.assertEquals(self.task.project.title, 'Test Project')

    def test_task_project_data_description(self):
        self.assertEquals(self.task.project.description, 'Test Content Description')

    def test_task_project_user_data(self):
        self.assertEquals(self.project.owner, self.test_user)
        self.assertEquals(self.task.project.owner, self.test_user)

    def test_created_label(self):
        field_label = self.task._meta.get_field('created').verbose_name
        self.assertEquals(field_label, 'created')

    def test_created_date(self):
        date = self.task.created.date().today()
        self.assertEquals(date, datetime.date.today())

    def test_due_date_label(self):
        field_label = self.task._meta.get_field('due_date').verbose_name
        self.assertEquals(field_label, 'due date')

    def test_due_date_date(self):
        due_date = self.task.created.date().today()
        self.assertEquals(due_date, datetime.date.today())

    def test_complete_label(self):
        field_label = self.task._meta.get_field('complete').verbose_name
        self.assertEquals(field_label, 'complete')

    def test_complete_data_equal(self):
        self.assertEquals(self.task.complete, False)

    def test_complete_data_not_equal(self):
        self.assertNotEquals(self.task.complete, True)

    def test_slug_label(self):
        field_label = self.task._meta.get_field('slug').verbose_name
        self.assertEquals(field_label, 'slug')

    def test_slug_max_length(self):
        max_length = self.task._meta.get_field('slug').max_length
        self.assertEquals(max_length, 250)

    def test_object_name(self):
        expected_object_name = f'{self.task.project}: {self.task.title}'
        self.assertEquals(expected_object_name, str(self.task))
