# forms.py

from django import forms

class OrderForm(forms.Form):
    menu_name = forms.CharField(max_length=100)
    price = forms.IntegerField(widget=forms.HiddenInput())
    quantity = forms.IntegerField()
    total_price = forms.IntegerField(widget=forms.HiddenInput())


"""
from django import forms

class CommentForm(forms.Form):
    name = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class' :'form-control', 'placeholder' : 'name' }))
    comment = forms.CharField(widget=forms.Textarea(attrs={'class' :'form-control', 'placeholder' : 'comment' }))

"""
