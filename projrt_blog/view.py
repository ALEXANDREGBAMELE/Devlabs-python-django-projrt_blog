from django.http import HttpResponse
from django.shortcuts import render

def home_view(request):
    # return HttpResponse('Hello world!')
    return render(request, 'home.html')
def contact(request):
    # return HttpResponse('Contactez nous!')
    return render(request, 'contact.html')

def articles_view(request):
    return render(request, 'article.html')