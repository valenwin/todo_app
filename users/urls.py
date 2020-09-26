from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from django_registration.backends.one_step.views import RegistrationView

from .forms import CustomSignUpForm
from .views import RegistrationCompleteView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('accounts/register/', RegistrationView.as_view(
        form_class=CustomSignUpForm,
        success_url='/'),
         name='django_registration_register'),
    path('register/complete', RegistrationCompleteView.as_view(),
         name='django_registration_register_complete'),

]
