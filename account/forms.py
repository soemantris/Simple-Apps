from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from . models import User


class UpdateUserForms(UserChangeForm):
    class Meta:
        model = User
        fields = [
            'nama', 'tmp_lahir', 'email', 'tgl_lahir', 'no_hp', 'img_user'
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['nama'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Masukan nama lengkap Anda'})
        self.fields['tmp_lahir'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Masukan tempat lahir Anda'})
        self.fields['tgl_lahir'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Masukan tanggal lahir Anda'})
        self.fields['email'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Masukan email Anda'})
        self.fields['no_hp'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Masukan no hp Anda'})
        self.fields['img_user'].widget.attrs.update(
            {'class': 'form-control'})


class RegisterUserForms(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'nama', 'no_hp', 'email', 'password1', 'password2',
        ]
