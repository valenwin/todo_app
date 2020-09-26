from django import forms
from django.contrib.auth.models import User
from django_registration.forms import RegistrationFormUniqueEmail


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())


class CustomSignUpForm(RegistrationFormUniqueEmail):
    email = forms.EmailField(max_length=150, help_text='eg. youremail@mail.com',
                             widget=forms.EmailInput())

    class Meta(RegistrationFormUniqueEmail.Meta):
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
