from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    if request.method == 'POST':
        return HttpResponse("<h1>You must have POSTed something!</h1>")
    else:
        return HttpResponse(request.method)