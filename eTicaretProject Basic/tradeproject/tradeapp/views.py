from django.shortcuts import render
from . import models
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView

# Create your views here.

def mainpage(request):
    return render(request, 'tradeapp/mainpage.html')

def clothes(request):
    return render(request, 'tradeapp/clothes.html')

def sweater(request):
    return render(request, 'tradeapp/sweater.html')
    
def tshirt(request):
    return render(request, 'tradeapp/tshirt.html')

def pants(request):
    return render(request, 'tradeapp/pants.html')

def shopbag(request):
    return render(request, 'tradeapp/shopbag.html')

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
