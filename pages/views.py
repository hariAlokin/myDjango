from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# First param = wsgi_request, so
def home(request, *args, **kwargs):
    # return HttpResponse("<h1>Hello World!</h1>")
    return render(request, 'home.html', {})

def contact(request, *args, **kwargs):
    return render(request, 'contact.html', {})