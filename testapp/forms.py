from cProfile import label
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from . models import Project_model


class RegisterForm(UserCreationForm):

    password1 = forms.CharField(label='Enter your password' ,widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Confirm your password' ,widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:

        model = User

        fields = ['username','first_name','last_name','email']

        widgets = {
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
        }


class LoginForm(AuthenticationForm):

    username = forms.CharField(label='Enter your username',widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(label='Enter your password' ,widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:

        model = User

        fields = ['username','password']

class Project_Form(forms.ModelForm):

    class Meta:

        model=Project_model

        fields=['title','desc']

        labels={
            'title':'Enter your Project title',
            'desc':'Enter your Project description'
            
        }

        widgets={
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'desc':forms.Textarea(attrs={'class':'form-control'})
            
        }


