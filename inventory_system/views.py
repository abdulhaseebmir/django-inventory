from articles.models import Article
from django.http import HttpResponse

def home_view(request):
    article = Article.objects.get(id=1)
    html_string = f"""
    <h2>{article.title}</h2>
    <p>{article.content}</p>
    """
    return HttpResponse(html_string)