from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth import get_user_model

User = get_user_model()

class NewUserCreationForm(UserCreationForm):
	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

# https://stackoverflow.com/questions/55369645/how-to-customize-default-auth-login-form-in-django
class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = UsernameField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': ''}))
