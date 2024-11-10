from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
from . forms import SendingEmailForm


def index(request):
    if request.method == "POST":
        form = SendingEmailForm(request.POST or None)
        if form.is_valid():
            subjek = form.cleaned_data['subject']
            email = form.cleaned_data['email']
            nama = form.cleaned_data['name']
            pesan = form.cleaned_data['message']
            send_mail(subjek,  # ini subjek
                      f"pesan dari {nama} dengan email <{email}>\n\n"
                      f"Pesannya: {pesan}",  # ini pesannya yang di kirimkan
                      None,  # ini dari email
                      [settings.EMAIL_HOST_USER],  # ganti dengan email Anda
                      )
            return redirect('/kontak/')

    else:
        form = SendingEmailForm()

    context = {
        'title': 'Kontak',
        'form': form,
    }
    return render(request, 'contact/index.html', context)
