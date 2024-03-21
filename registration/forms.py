from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
         'placeholder':'your username',
        # for using bootstrap classes write here
        'class':'bg-black'
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
         'placeholder':'your password',
        # for using bootstrap classes write here
        'class':'bg-black'
    }))


# class SignupForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = {'username','email','password1','password2'}
#         username = forms.CharField(widget=forms.TextInput(attrs={
#         'placeholder':'your username',
#         # for using bootstrap classes write here
#         'class':'bg-black'
#     }))    

#     email = forms.CharField(widget=forms.EmailInput(attrs={
#         'placeholder':'your email address',
#         # for using bootstrap classes write here
#         'class':'bg-black'
#     }))    
    
#     password1 = forms.CharField(widget=forms.PasswordInput(attrs={
#         'placeholder':'your password',
#         # for using bootstrap classes write here
#         'class':'bg-black'
#     }))    
    
#     password2 = forms.CharField(widget=forms.PasswordInput(attrs={
#         'placeholder':'repeat the password',
#         # for using bootstrap classes write here
#         'class':'bg-black'
#     })) 
    
class SignupForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'your username',
        'class': 'bg-black'
    }))

    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder': 'your email address',
        'class': 'bg-black'
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'your password',
        'class': 'bg-black'
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'repeat the password',
        'class': 'bg-black'
    }))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
