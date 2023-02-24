from articles.models import Article
from django.shortcuts import render

def home_view(request):
    article = Article.objects.get(id=1)
    articles = Article.objects.all()
    context = {
        "articles": articles,
        "id": article.id,
        "title": article.title,
        "content": article.content
    }
    # html_string = """
    # <h2>{title} (id: {id})</h2>
    # <p>{content}</p>
    # """.format(**context)
    return render(request, "home-view.html", context)