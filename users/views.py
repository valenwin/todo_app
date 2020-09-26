from django.views.generic import TemplateView


class RegistrationCompleteView(TemplateView):
    template_name = 'django_registration/registration_closed.html'
