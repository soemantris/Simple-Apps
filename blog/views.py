from django.shortcuts import render
from django.core.paginator import Paginator
# Create your views here.
from . models import Article, Category, Comment
from . forms import CommentsForm


def index(request):
    list_articles = Article.objects.all().order_by('-publish')
    list_categories = Category.objects.all()

    # add paginations
    p = Paginator(list_articles, 10)
    page_number = request.GET.get("page")
    articles = p.get_page(page_number)

    context = {
        'title': 'Blog',
        # 'list_articles': list_articles,
        'categories': list_categories,
        'articles': articles,
    }
    return render(request, 'blog/index.html', context)


def detail(request, slug_input):
    detail_article = Article.objects.get(slug=slug_input)
    article_terkait = Article.objects.exclude(slug=slug_input)
    # varibel tampilan komentar
    comments_article = Comment.objects.filter(
        articles=detail_article, reply=None).order_by('-timestamp')

    # add script komentar
    if request.method == 'POST':
        form = CommentsForm(request.POST or None)
        if form.is_valid():
            comment = request.POST.get('comments')
            reply = request.POST.get('comment_slug')
            comments = None
            if reply:
                comments = Comment.objects.get(id=reply)
            comment = Comment.objects.create(
                articles=detail_article, user=request.user, comments=comment, reply=comments)
            form = CommentsForm()
    else:
        form = CommentsForm()

    context = {
        'title': 'Detail',
        'detail_article': detail_article,
        'article_terkait': article_terkait,
        # variabel objek komentar
        'form': form,
        'comments': comments_article,
    }
    return render(request, 'blog/detail.html', context)


def category(request, category_input):
    category_articles = Article.objects.filter(
        categories__title=category_input)
    category_choices = Category.objects.order_by('id')
    context = {
        'title': 'Artikel berdasarkan kategori',
        'category_articles': category_articles,
        'category_choices': category_choices,
    }
    return render(request, 'blog/category.html', context)
