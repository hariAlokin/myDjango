from django.core.validators import RegexValidator
from django import forms
from django.forms import widgets

from .models import *

PHONE_REGEX_VALIDATOR = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")

class ContactForm(forms.Form):
    name = forms.CharField(max_length=250)
    organisation = forms.CharField(max_length=250, required=False)
    email = forms.EmailField(required=False)
    phone = forms.CharField(validators=[PHONE_REGEX_VALIDATOR], max_length=100, required=False)
    message = forms.CharField(widget=widgets.Textarea,max_length=250, required=False)