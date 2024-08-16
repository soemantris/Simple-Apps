from django.shortcuts import render

# Create your views here.
from . models import Artcile, Category


def index(request):
    list_articles = Artcile.objects.all().order_by('-publish')
    context = {
        'title': 'Blog',
        'articles': list_articles,
    }
    return render(request, 'blog/index.html', context)


def detail(request, slug_input):
    detail_article = Artcile.objects.get(slug=slug_input)
    context = {
        'title': 'Detail',
        'detail_article': detail_article,
    }
    return render(request, 'blog/detail.html', context)
