from articles.models import Article
from django.http import HttpResponse

def home_view(request):
    article = Article.objects.get(id=1)
    context = {
        "id": article.id,
        "title": article.title,
        "content": article.content
    }
    html_string = """
    <h2>{title} (id: {id})</h2>
    <p>{content}</p>
    """.format(**context)
    return HttpResponse(html_string)