from django.shortcuts import render
from django.http import HttpResponse

# View to handle empty domain link (index page)
def index(request):
    return HttpResponse("Rango says hey there partner!" + " <a href='/rango/about/'>About</a>")

def about(request):
    return HttpResponse("Rango says here is the about page." + " <a href='/rango/'>Index</a>.")