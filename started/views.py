from django.shortcuts import render

# Create your views here.

from cgitb import html
from django.shortcuts import redirect

def home(request):
    return render(request,'started/includes/home.html')

def record_audio(request):
    return render(request,'started/includes/record_audio.html')    

def new_rec(request):
    return render(request,'started/includes/new_rec.html')