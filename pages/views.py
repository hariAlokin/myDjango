from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm

# Create your views here.
# First param = wsgi_request, so
def home(request, *args, **kwargs):
    # return HttpResponse("<h1>Hello World!</h1>")
    return render(request, 'home.html', {})

def contact(request, *args, **kwargs):
    form = ContactForm(request.POST or None)
    my_context = {
        "organisation": "Kryptonite",
        "email": "hari.kb116@gmail.com",
        "phone": 9074146503,
        "form": form
    }
    if request.method == 'POST':
        if form.is_valid():
            print(form.cleaned_data)
            print(form.errors)
            form = ContactForm()
    return render(request, 'contact.html', my_context)
