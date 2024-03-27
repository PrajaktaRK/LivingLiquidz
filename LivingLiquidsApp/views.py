from multiprocessing import context
from django.shortcuts import render, redirect
from .models import spirits_indian_whiskey


def default_view(request):    
    return render(request, 'Home.html')

def spirits_indian_whiskey(request):
    return render(request, 'Blended_Whiskey.html')







