from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Article

# Create your views here.

def article_search_view(request):
    query_dict = request.GET
    try:
        query = int(query_dict.get("query")) # see also: query_dict["query"]
    except:
        query = None
    article_object = None
    if query:
        article_object = Article.objects.get(id=query)
    context = {
        "article_object": article_object
    }
    return render(request, "articles/search.html", context)

@login_required
def article_create_view(request):
    if request.method == "POST":
        title = request.POST.get("title") # see also POST["title"]
        content = request.POST.get("content") 
        Article.objects.create(title=title, content=content)
    context = {}
    return render(request, "articles/create.html", context=context)

def article_detail_view(request, id=None):
    article_object = None
    if id:
        article_object = Article.objects.get(id=id)
    context = {
        "object": article_object
    }
    return render(request, "articles/detail.html", context=context)