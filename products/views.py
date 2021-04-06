from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.

# def product_create(request, *args, **kwargs):
def product_index(request, *args, **kwargs):
    p_list = Product.objects.filter(active=True)
    return render(request, "products/index.html", {"product_list": p_list})

def product_detail(request):
    p_obj = Product.objects.get(id=3)
    p_context = {
        "name": p_obj.name,
        "description": p_obj.description,
        "price": p_obj.price
    }
    return render(request, 'products/detail.html', p_context)

# def product_update(request, *args, **kwargs):
# def product_delete(request, *args, **kwargs):
