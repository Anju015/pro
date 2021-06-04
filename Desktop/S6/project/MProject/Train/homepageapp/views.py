from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from . models import reg_tbl


def register(request):
   # return render(request,'signup.html')

    if request.method=="POST" :
       name = request.POST.get("name")
       age = request.POST.get("age")
       gender = request.POST.get("gender")
       email = request.POST.get("email")
       phone = request.POST.get("phone")
       uname = request.POST.get("uname")
       passwd = request.POST.get("pass")
       obj=reg_tbl(name=name,age=age,gender=gender,phone=phone,uname=uname,paswd=passwd,eml=email)
       obj.save()
       if obj:
        msg="saved successfully"
        return render(request,"signup.html",{"reg":msg})
    else:
        return render(request,"signup.html")


    return render(request, "signup.html")

def home(request):
    return render(request,'signup.html')

def index(request):
    return render(request,'index.html')

def vi(request):
    viobj = reg_tbl.objects.all()
    return render(request,'viewdata.html',{'data':viobj})
