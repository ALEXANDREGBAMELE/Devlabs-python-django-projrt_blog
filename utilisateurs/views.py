from django.http import HttpResponse
from django.shortcuts import render
from urllib3 import HTTPResponse

# Create your views here.
def utilisateurs_view(request):
    return render(request,'utilisateurs/liste.html')

def utilisateurs_view(request):
    return HttpResponse("Page de creation d'utilisateur")
