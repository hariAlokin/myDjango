from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *
# Create your views here.

"""Products"""
def product_create(request, *args, **kwargs):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        print(form.save())
        form = ProductForm()
    context = {'form': form}
    return render(request, 'products/create.html', context)

def product_index(request, *args, **kwargs):
    p_list = Product.objects.filter(active=True)
    return render(request, "products/index.html", {"product_list": p_list})

def product_detail(request, p_id):
    # print(p_id)
    p_obj = Product.objects.get(id=p_id)
    p_context = {
        "name": p_obj.name,
        "description": p_obj.description,
        "price": p_obj.price
    }
    return render(request, 'products/detail.html', p_context)

# def product_update(request, *args, **kwargs):
# def product_delete(request, *args, **kwargs):
