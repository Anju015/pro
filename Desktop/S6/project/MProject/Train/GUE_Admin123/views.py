from django.shortcuts import render, redirect
from GUE_Employee.models import emp_reg_tbl
from .models import pdt_reg_tbl,sup_reg_tbl,stocks,cat_reg_tbl,machine_req_tbl
from GUE_Customer.models import  cust_reg_tbl
from homepageapp.models import  adminlogin

#Admin home page load
def home(request):
    return render(request,'Admin_Basic.html')


def adminhome(request):
    msg = request.GET.get("msg")
    if msg:
        return render(request, 'Admin_Basic.html', {'msg': msg})
    else:
        msg=" "
        return render(request, 'Admin_Basic.html',{'msg':msg})

###############################################Registraton pages################################
#employee registration
def emp_register(request):
    if request.method == "POST":
        empname = request.POST.get("name")
        address = request.POST.get("address")
        gender = request.POST.get("gender")
        age = request.POST.get("age")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        designation = request.POST.get("des")
        dept = request.POST.get("dept")
        dtime = request.POST.get("dtime")
        uname = request.POST.get("uname")
        passwd = request.POST.get("passw")
        obj1 = emp_reg_tbl(empname=empname,address=address,gender=gender,age=age,email=email,
               phone=phone,designation=designation,dept=dept,dtime=dtime,uname=uname,passwd=passwd)
        obj1.save()
        if obj1:
            msg = "saved successfully"
            return  redirect("/GUE_Admin123/home?msg=saved successfully")

    else:

      return render(request, "Employee_Reg.html")

    return  render(request,'Employee_Reg.html')

## Product registration

def product_reg(request):
    if request.method == "POST":
        pdtname = request.POST.get("pdtname")
        pdtimage = request.FILES.get("pdtimage")
        pdtprice = request.POST.get("pdtprice")
        pdttax = request.POST.get("pdttax")
        pdtquality = request.POST.get("pdtquality")
        pdtstatus = request.POST.get("pdtstatus")
        category=request.POST.get("category")
        obj2 = pdt_reg_tbl(pdtname=pdtname, pdtimage=pdtimage, pdtprice=pdtprice, pdttax=pdttax, pdtquality=pdtquality,
                           pdtstatus=pdtstatus,category=category)
        obj2.save()
        if obj2:
            if request.GET.get("type") == "ADM":
                return redirect("/GUE_Admin123/home?msg=saved successfully")
            if request.GET.get("type") == "EMP":
                return redirect("/GUE_Employee/home?msg=saved successfully")

    else:
        cat=cat_reg_tbl.objects.all()
        return render(request, "Product_Reg.html",{'cat':cat})


#supplier registration......

def supplier_reg(request):
    if request.method == "POST":
       supname = request.POST.get("supname")
       contact = request.POST.get("contact")
       company = request.POST.get("company")
       obj2 = sup_reg_tbl(supname=supname, contact=contact,company=company)
       obj2.save()
       if obj2:
           msg = "saved successfully"
           return redirect("/GUE_Admin123/home?msg=saved successfully")
    else:
       return render(request, "Supplier_Reg.html")

#stock management
def stock(request):
    if request.method == "POST":
        prodid = request.POST.get("productid")
        stock = request.POST.get("stock")
        emp_obj = pdt_reg_tbl.objects.get(id=prodid)
        obj2 = stocks(productid=emp_obj, stock=stock)
        obj2.save()
        if obj2:
            msg = "saved successfully"
            return redirect("/GUE_Admin123/home?msg=saved successfully")
    else:
        return render(request, "Admin_Stock_Management.html")


# product category add
def category_add(request):
   if request.method == "POST":
       pdtcatname = request.POST.get("pdtcatname")
       pdtcatstatus = request.POST.get("pdtcatstatus")
       obj2 = cat_reg_tbl(pdtcatname=pdtcatname, pdtcatstatus=pdtcatstatus)
       obj2.save()
       if obj2:
           msg = "saved successfully"
           return redirect("/GUE_Admin123/home?msg=saved successfully")
   else:
     return render(request, "Admin_Category_add.html")


# machine request

def machinereq(request):
    if request.method == "POST":
        machinename = request.POST.get("machinename")
        status = request.POST.get("status")
        empid = request.POST.get("empid")
       # empid=int(empid)
        empname = request.POST.get("empname")
        emp_obj = emp_reg_tbl.objects.get(id=empid)
        obj2 = machine_req_tbl(machinename=machinename,status=status,empid=emp_obj,empname=empname)
        obj2.save()
        if obj2:
            msg = "saved successfully"
            return redirect("/GUE_Admin123/home?msg=saved successfully")
    else:
        return render(request, "Machinary_Req.html")

#---------------------------------------------------------------------------------------------------------#
                                    #view pages
#---------------------------------------------------------------------------------------------------------#
# view Employee data (fetching)
def viemp(request):
   viobj = emp_reg_tbl.objects.all()
   return render(request, 'Emp_reg_view.html', {'data': viobj})

# view Product category
def vicat(request):
   viobj = cat_reg_tbl.objects.all()
   return render(request, 'cat_view.html', {'data': viobj})

#view customer
def vicust(request):
   viobj = cust_reg_tbl.objects.all()
   return render(request, 'cust_view.html', {'data': viobj})
#view supplier
def visup(request):
    viobj = sup_reg_tbl.objects.all()
    return render(request, 'sup_view.html', {'data': viobj})
#view product
def vipdt(request):
    viobj = pdt_reg_tbl.objects.all()
    return render(request, 'product_view.html', {'data': viobj})
#view stock
def vistock(request):
    viobj = stocks.objects.all()
    return render(request, 'stock_view.html', {'data': viobj})
#product Edit
def edt(request):

    if request.method=="POST":
        idno=request.POST.get("idn")
        pdtimage = request.FILES.get("pdtimage")
        pdtname=request.POST.get("pdtname")
        pdtprice = request.POST.get("pdtprice")
        pdttax =request.POST.get("pdttax")
        pdtquality= request.POST.get("pdtquality")
        pdtstatus=request.POST.get("pdtstatus")
        category =request.POST.get("category")

        upd=pdt_reg_tbl.objects.get(id=idno)
        if pdtimage!="":
            upd.pdtimage=pdtimage
        upd.pdtimage=upd.pdtimage
        upd.pdtname=pdtname
        upd.pdtprice = pdtprice
        upd.pdttax = pdttax
        upd.pdtquality = pdtquality
        upd.pdtstatus = pdtstatus
        upd.category = category

        upd.save()
        obj=pdt_reg_tbl.objects.all()
        return render(request,'product_view.html',{'msg':'data updated',"data":obj})
    else:
        obj = pdt_reg_tbl.objects.all()
        return render(request,'product_view.html',{'msg':'',"data":obj})



#home
def home(request):
    user=request.session['username']
    passw=request.session['password']
    if user=="" and passw=="":
        return redirect("/GUE_Admin123/logout")
    else:
        return render(request,'Admin_Basic.html')
#login
def login(request):
    if request.method=="POST":
        user=request.POST.get("username")
        passw=request.POST.get("passw")
        obj=adminlogin.objects.filter(username=user,password=passw)
        if obj:

            request.session['username']=user
            request.session['password']=passw
            return redirect("/GUE_Admin123/home")
        else:
            msg="incorrect password or username"
            return render(request,'adminlogpage.html',{'msg':msg})
    else:
        msg=""
        return render(request,'adminlogpage.html',{'msg':msg})
def logout(request):
    request.session['username']=""
    request.session['password']=""
    return render(request,'adminlogpage.html')


# view Employee data (fetching)
def viemp(request):
   viobj = emp_reg_tbl.objects.all()
   return render(request, 'Emp_reg_view.html', {'data': viobj})

def delt(request):
    idno=request.GET.get('idn')
    obj2=emp_reg_tbl.objects.get(id=idno)
    obj2.delete()
    return redirect("/GUE_Admin123/empview")

def emp_view(request):
    obj=emp_reg_tbl.objects.all()
    return render(request,'emp_view_admin.html',{'data':obj})







# Create your views here.
#from django.shortcuts import render
#from .models import  pdt_reg_tbl, pdt_category_add,machine_add,stocks12


#from GUE_Supplier.models import supplier_reg_table



# Create your views here.
from django.http import HttpResponse


# # Create your views here.
# from . models import reg_tbl

# employee registration

# return render(request, "signup.html")

# admin home page call



#update employee details

#def update(request):
 #   if request.method == "POST":
  #      a = request.POST.get("tname")
   #     b = request.POST.get("address")
    #    c = request.POST.get("tdesignation")
     #   e = request.POST.get("gender")
      #  f = request.POST.get("email")
      #  g = request.POST.get("phoneno")
      #  h = request.POST.get("dept")
       # i = request.POST.get("dt")
       # j = request.POST.get("passw")
       # k=request.POST.get("username")
        #idno = request.POST.get("empid")
     #   upobj = emp_reg_tbl.objects.get(id=idno)
      #  upobj.empname = a
      #  upobj.age = b
      #  upobj.designation = c
      #  upobj.gender = e
      #  upobj.phone = f
      #  upobj.dept = g
       # upobj.dtime = h
       # upobj.empsalary = i
       # upobj.uname = j
       # upobj.UPDATE()

      #  return redirect("/GUE_Admin123/viemp")
       # return render(request,'Edit_employee.html',{'employee': upobj})

# def index(request):
#    return render(request,'index.html')
# def vi(request):
#   viobj = reg_tbl.objects.all()
#  return render(request,'viewdata.html',{'data':viobj})

#def destroy(request, id):
   # employee = emp_reg_tbl.objects.get(id=id)
   # employee.delete()
    #return redirect("/viemp")




















# view supplier details(fetching data)
#def visup(request):
 #   viobj = supplier_reg_table.objects.all()
  #  return render(request, 'Sup_reg_view.html', {'data': viobj})

# def index(request):
#   return render(request,"index.html")
