from django.urls import path
# from .views import hello
from django.contrib.auth import views as auth_views
from . import views
from .import forms

app_name = 'registration'
urlpatterns = [
    path('',views.hello),
    path('signup',views.signup,name='signup'),
    path('login/',auth_views.LoginView.as_view(template_name = 'login.html',authentication_form = forms.LoginForm),name='login')
]
