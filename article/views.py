from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from article.models import Article
from .forms import ArticleForm
from django.contrib import messages
# Create your views here.


def index(request):
    context = {
        "numbers": [1, 2, 3, 4, 5, 6],
        "number2": 20
    }
    return render(request, "index.html", context)


def about(request):
    return render(request, "about.html")


def dashboard(request):

    articles = Article.objects.filter(author=request.user)

    context = {
        'articles': articles
    }

    return render(request, "articles/dashboard.html", context=context)


def add(request):
    form = ArticleForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        article = form.save(commit=False)

        article.author = request.user

        article.save()

        messages.success(request, "Makale Başarıyla Oluşturuldu")

        return redirect("article:dashboard")
    context = {
        'form': form
    }
    return render(request, "articles/add.html", context=context)


def update(request, id):
    return HttpResponse(id)


def delete(request, id):
    return HttpResponse(id)


def detail(request, id):
    article = get_object_or_404(Article, id=id)
    return render(request, "articles/detail.html", {"article": article})


def custom_page_not_found_view(request, exception):
    return render(request, "errors/404.html", {})
