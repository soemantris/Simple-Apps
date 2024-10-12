from django.shortcuts import render, redirect
from django.contrib.auth import logout

# Create your views here.
from . forms import RegisterUserForms, UpdateUserForms


def index_profiles(request):

    context = {
        'title': 'Data Profiles',
    }
    return render(request, 'account/profile.html', context)


def update_profiles(request):
    if request.method == 'POST':
        form = UpdateUserForms(request.POST or None,
                               request.FILES or None, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('/accounts/')
    else:
        form = UpdateUserForms(instance=request.user)

    context = {
        'title': 'Edit Data Profiles',
        'form': form,
    }
    return render(request, 'account/edit_profile.html', context)


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
