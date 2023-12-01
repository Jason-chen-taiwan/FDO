from django import forms

class LoginForm(forms.Form):
    name = forms.CharField(label="Your name")
    password = forms.CharField(label="Your password")

class RegisterForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    email = forms.EmailField(label='Email')
    password = forms.CharField(label='Password', widget=forms.PasswordInput())
    identity = forms.MultipleChoiceField(
        required=True,
        widget=forms.CheckboxSelectMultiple,
        choices=(('option1', 'manufacture'), ('option2', 'Rendezvous'), ('option3', 'Owner')),  # 根据需要定义选项
        label="Identity"
    )