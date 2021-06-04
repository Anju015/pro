from django.shortcuts import render,redirect
from .models import cust_reg_tbl
#from . models import cust_reg_tbl,cust_feedback_tbl
#from django.shortcuts import render

def home(request):
    return render(request,"customer_home.html")



#customer registration
def customer_registration(request):
   if request.method == "POST":
       name = request.POST.get("name")
       address = request.POST.get("address")
       contact = request.POST.get("contact")
       email = request.POST.get("email")
       uname = request.POST.get("uname")
       password1 = request.POST.get("password1")
       obj1 = cust_reg_tbl(name=name, address=address,contact=contact,email=email,uname=uname,password1=password1)
       obj1.save()
       if obj1:
           msg = "saved successfully"
           return redirect("/GUE_Admin123/home?msg=saved successfully")
   else:
       return render(request, "Customer_Reg.html")
##customer feedback
#def customer_feedback(request):
 #   if request.method == "POST":
 #       custname = request.POST.get("custname")
 #       comments = request.POST.get("comments")
 #       email = request.POST.get("email")
 #       obj1 = cust_feedback_tbl(custname=custname, comments=comments,email=email)
  #      obj1.save()
   #     if obj1:
   #         msg = "saved successfully"
    #        return render(request, "Feedback.html", {"reg": msg})
   # else:
   #     return render(request, "Feedback.html")

# view customer details...
#def viewcust(request):
 #   viobj = cust_reg_tbl.objects.all()
 #   return render(request,'cust_reg_view.html',{'data':viobj})

# Create your views here.
