from multiprocessing import context
from django.shortcuts import render
from article.models import Article, Category, Comment
from .forms import CommentForm

# Create your views here.
def article_category(request, category):
    articles = Article.objects.filter(
        categories__name__contains=category
    ).order_by('created_on')
    context = {
        "category": category,
        "articles": articles
    }
    return render(request, "articles/article_category.html", context)

def article_index(request):
    articles = Article.objects.all().order_by('created_on')
    context = {
        "articles": articles,
    }
    return render(request, "articles/article_index.html", context)


def article_detail(request, pk):
    article = Article.objects.get(pk=pk)
    comments = Comment.objects.filter(article=article)
    context = {
        "article": article,
        "comments": comments,
    }
    form= CommentForm()
    if request.method == "POST":
        form= CommentForm(request.POST)
        if form.is_valid():
            comment= Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                article=article
            )
            comment.save()

    comments= Comment.objects.filter(article=article)
    context= {
        "article": article,
        "comments": comments,
        "form": form,
    }
    return render(request, "articles/article_detail.html", context)

