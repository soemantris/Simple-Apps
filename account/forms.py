from django.contrib.auth.forms import UserCreationForm
from . models import User


class RegisterUserForms(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'nama', 'no_hp', 'email', 'password1', 'password2',
        ]
