from django.http import HttpResponse
from django.shortcuts import render

from .db_articles import articles
def home_view(request):
    # return HttpResponse('Hello world!')
    return render(request, 'home.html')
def contact_view(request):
    # return HttpResponse('Contactez nous!')
    return render(request, 'contact.html')
    # return HttpResponse('La liste des articles!')
def articles_view(request):
    return render(request, 'article.html', context={'articles' : articles})