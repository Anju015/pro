from django.shortcuts import render,redirect
from .models import pdt_req_tbl
# Create your views here.
def home(request):
   return render(request, 'Employee_home.html')

def pdt_req(request):
      if request.method == "POST":
         pdtname = request.POST.get("pdtname")
         qty = request.POST.get("qty")
         supname = request.POST.get("supname")
         obj2 = pdt_req_tbl(pdtname=pdtname,qty=qty,supname=supname)
         obj2.save()
         if obj2:
            msg = "saved successfully"
            return redirect("/GUE_Supplier/home?msg=saved successfully")
      else:
         return render(request, "pdt_req.html")
