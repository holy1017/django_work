from django.shortcuts import render
from django.template.context_processors import request

# Create your views here.

def hello(request):
    return render(request, "hello.html")