from django.shortcuts import render

def index(request):
    return render("hello world")

def detail(request,p1):
    return render(p1)