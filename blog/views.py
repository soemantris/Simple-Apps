from django.shortcuts import render

# Create your views here.
from . models import Artcile, Category


def index(request):
    list_articles = Artcile.objects.all().order_by('-publish')
    list_categories = Category.objects.all()
    context = {
        'title': 'Blog',
        'articles': list_articles,
        'categories': list_categories,
    }
    return render(request, 'blog/index.html', context)


def detail(request, slug_input):
    detail_article = Artcile.objects.get(slug=slug_input)
    article_terkait = Artcile.objects.exclude(slug=slug_input)
    context = {
        'title': 'Detail',
        'detail_article': detail_article,
        'article_terkait': article_terkait,
    }
    return render(request, 'blog/detail.html', context)


def category(request, category_input):
    category_articles = Artcile.objects.filter(
        categories__title=category_input)
    category_choices = Category.objects.order_by('id')
    context = {
        'title': 'Artikel berdasarkan kategori',
        'category_articles': category_articles,
        'category_choices': category_choices,
    }
    return render(request, 'blog/category.html', context)
