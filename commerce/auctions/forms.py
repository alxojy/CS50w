from django.forms import ModelForm
from django import forms

from .models import Listing, Bid, Comment, Category

class CreateListingForm(forms.Form):
    title = forms.CharField(label="Title")
    description = forms.CharField(widget=forms.Textarea(attrs={'rows':'5', 'cols':'50'}))
    bid = forms.CharField(widget=forms.NumberInput(attrs={'step':'0.01', 'min':'0'}))
    image_url = forms.CharField(widget=forms.URLInput())