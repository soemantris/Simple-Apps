from django.shortcuts import render

# Create your views here.


def index(request):
    context = {
        'title': 'Blog',
    }
    return render(request, 'blog/index.html', context)


def detail(request):
    context = {
        'title': 'Detail',
    }
    return render(request, 'blog/detail.html', context)
