from django.shortcuts import render
from django.http import HttpResponse

# View to handle empty domain link (index page)
def index(request):
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
    return render(request, 'rango/index.html', context=context_dict)

# View for the about page 
def about(request):
    context_dict = {'boldmessage': 'This tutorial has been put together by Ibrahim Hassan.'}
    return render(request, 'rango/about.html', context=context_dict)
