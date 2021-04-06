from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# First param = wsgi_request, so
def home(request, *args, **kwargs):
    # return HttpResponse("<h1>Hello World!</h1>")
    return render(request, 'home.html', {})

def contact(request, *args, **kwargs):
    my_context = {
        "organisation": "Kryptonite",
        "email": "hari.kb116@gmail.com",
        "phone": 9074146503
    }
    return render(request, 'contact.html', my_context)

def product_detail(request, *args, **kwargs):
    p_context = {
        "name": "Mac book air pro",
        "description": "The most amazing product ever!",
        "price": "1,50,000/- Rs"
    }
    return render(request, 'products/detail.html', p_context)