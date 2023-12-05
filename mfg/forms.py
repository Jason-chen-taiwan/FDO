# forms.py
from django import forms

class ServerInfoForm(forms.Form):
    url = forms.CharField(label='URL', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Enter URL'}))
    ip = forms.CharField(label='IP Address', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Enter IP Address'}))
    port = forms.CharField(label='Port', max_length=10, widget=forms.TextInput(attrs={'placeholder': 'Enter Port Number'}))

class OwnerInfo(forms.Form):
    url = forms.CharField(label='URL', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Enter URL'}))