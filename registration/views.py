from django.shortcuts import render
from .forms import SignupForm
# Create your views here.

def signup(request):
    form = SignupForm()
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'login.html')   
    return render(request,'signup.html',{'form':form})     

def hello(request):
    return render(request,'intro.html')