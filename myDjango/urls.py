"""myDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from pages.views import home, contact
from products.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    # own
    path('', home, name="home"),
    path('contact-us/', contact, name="contact"),
    path('products/', product_index, name="product_index"), 
    path('products/add/', product_create, name="product_create"), 
    path('products/<int:p_id>/', product_detail, name="product_detail"), 
    # path('products/3/edit/', product_update, name="product_update"), 
    # path('products/3/delete/', product_delete, name="product_delete"), 
]
