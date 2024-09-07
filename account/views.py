from django.shortcuts import render, redirect
from django.contrib.auth import logout

# Create your views here.
from . forms import RegisterUserForms


def register_users(request):
    if request.method == "POST":
        form = RegisterUserForms(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('/')

    else:
        form = RegisterUserForms()

    context = {
        'title': 'Form Register Users',
        'form': form,
    }
    return render(request, 'registration/daftar.html', context)


def LogoutView(request):
    logout(request)
    return redirect('/')
