from django.shortcuts import render


def index(request):
    context = {
        'title': 'Beranda',
    }
    return render(request, 'index.html', context)


def daftar(request):
    context = {
        'title': 'Daftar Akun',
    }
    return render(request, 'daftar.html', context)


def login(request):
    context = {
        'title': 'Login',
    }
    return render(request, 'login.html', context)
