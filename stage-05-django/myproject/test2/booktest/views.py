#coding=utf-8
from django.shortcuts import render
from .models import *
from django.db.models import Max,F,Q
from django.http import HttpResponse,HttpResponseRedirect

def index(request):
    # list = BookInfo.book1.filter(heroinfo__hcontent__contains="八")
    list = BookInfo.book1.filter(pk__lt=2)

    #聚合函数
    Max1 = BookInfo.book1.aggregate(Max('bpub_date'))

    # list = BookInfo.book1.filter(bread__gt=F('bcommet')) #阅读量大于评论量

    list = BookInfo.book1.filter(pk__gt=2,btitle__contains="八")

    list = BookInfo.book1.filter(Q(pk__lt=2) | Q(bcommet__gt=111))

    context = {'list':list,
               # 'Max1':Max1
               }
    return render(request,'booktest/index.html',context)

def detail(request,p1,p2,p3):
    return HttpResponse("%s-%s-%s"%(p1,p2,p3))

#================get请求方式===========
#测试链接
# http://127.0.0.1:8000/booktest/getTest2/?a=1&b=2&c=3

#展示链接的页面
def getTest1(request):
    return render(request,'booktest/getTest1.html')

#接收一键一值的情况
def getTest2(request):
    #根据见接收值
    a1 = request.GET['a']
    b1 = request.GET['b']
    c1 = request.GET['c']
    context = {'a':a1,'b':b1,'c':c1}
    #向模板中传递上下文,并渲染
    return render(request,'booktest/getTest2.html',context)

#接收一键多值的情况
def getTest3(request):
    a1 = request.GET.getlist('a')
    context={'a':a1}
    return render(request,'booktest/getTest3.html',context)

#================post请求方式===========
def postTest1(request):
    return render(request,'booktest/postTest1.html')

def postTest2(request):
    uname = request.POST['uname']
    upwd = request.POST['upwd']
    ugenger = request.POST.get('ugender')
    uhobby = request.POST.getlist('uhobby')
    context = {'uname':uname,'upwd':upwd,'ugender':ugenger,'uhobby':uhobby}
    return render(request,'booktest/postTest2.html',context)


#================cookie练习===========
def cookieTest(request):
    response = HttpResponse()
    cookie = request.COOKIES
    if 't1' in cookie:
        response.write(cookie['t1'])
    return response

    # response.set_cookie('t1','abc')
    return response

#================转向===========
def redTest1(request):
    return HttpResponseRedirect('/booktest/redTest2/')

def redTest2(request):
    return HttpResponse('这是转向来的页面')


#================通过用户登录练习session===========
def session1(request):
    uname = request.session.get('myname','未登录')
    context = {'uname':uname}
    return render(request,'booktest/session1.html',context)

def session2(request):
    return render(request,"booktest/session2.html")

def session2_handle(request):
    uname = request.POST['uname']
    request.session['myname'] = uname
    return HttpResponseRedirect('/booktest/session1/')

def session3(request):
    #删除session
    del request.session['myname']
    return HttpResponseRedirect('/booktest/session1/')
