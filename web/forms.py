# from pydoc import classname
from django import forms
from django.contrib.auth import authenticate
from web.models import Versions
class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)
    def __init__(self,*args,**kwargs):
        super().__init__()
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=150)
    password = forms.CharField(max_length=150,widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=150,widget=forms.PasswordInput,label="Password")
    first_name = forms.CharField(max_length=17)
    last_name = forms.CharField(max_length=17)

    def __init__(self,*args,**kwargs):
        super().__init__()
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


class UploadForm(forms.Form):
    file = forms.FileField(allow_empty_file=False )
    project = forms.CharField(label="project name" )
    address = forms.CharField(label="contract address")
    blockchain= forms.CharField()
    version = forms.ModelChoiceField(label="compiler version",queryset=Versions.objects.all().values_list("name",flat=True))

    def __init__(self,*args,**kwargs):
        super().__init__()
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
