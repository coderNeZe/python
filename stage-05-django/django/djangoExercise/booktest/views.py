from django.shortcuts import render
from django.http import *
# from django.template import RequestContext,loader
from .models import *

def index(request):
    # temp = loader.get_template('index.html')
    # return HttpResponse(temp.render())
    booklist = BookInfo.objects.all()
    print(booklist)
    context = {'list':booklist}
    return render(request,'index.html',context)

def show(request,id):
    book = BookInfo.objects.get(pk=id)
    herolist = book.heroinfo_set.all()
    print(herolist)
    context={'lsit':herolist}
    return render(request,'show.html',context)