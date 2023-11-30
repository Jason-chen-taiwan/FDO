from django import forms

class login(forms.Form):
    name = forms.CharField(label="Your name")
    password = forms.CharField(label="Your password")

class RegisterForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    email = forms.EmailField(label='Email')
    password = forms.CharField(label='Password', widget=forms.PasswordInput())