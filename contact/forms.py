from django.forms import ModelForm
from . models import Contact


class SendingEmailForm(ModelForm):
    class Meta:
        model = Contact
        fields = (
            'name', 'email', 'subject', 'message',
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Masukan nama lengkap anda.'})
        self.fields['email'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Masukan email anda.'})
        self.fields['subject'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Masukan subjek anda.'})
        self.fields['message'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Masukan pesan anda.'})
