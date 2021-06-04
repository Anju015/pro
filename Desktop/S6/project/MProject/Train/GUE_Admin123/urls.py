"""Train URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
   # path('admin/', admin.site.urls),
    path("admin/",views.home),

#emp registration...
     path("empreg",views.emp_register),

#product registration
     path("pdtreg",views.product_reg),

#supplier registration
     path("supreg",views.supplier_reg),

#product category add
     path("catadd",views.category_add),

##stock management
     path("stockadd",views.stock),

##machine req add
     path("mreq",views.machinereq),


path("home",views.adminhome),
######################################################## view data ########################
#emp data view
    path("empdvw",views.viemp),
#pdt cat data view
    path("pdtcatvi",views.vicat),
#cust view
    path("custvi",views.vicust),
#supplier view
   path("supdvw",views.visup),
#product view
    path("pdtvi",views.vipdt),
#stock view
    path("stockvi",views.vistock),
#employee update
  #   path("update/<int:id>",views.update),
   #  path('delete/<int:id>', views.destroy),


path("",views.login),
path("home",views.home),
path("logout",views.logout),
path("empview",views.emp_view),
path("delt",views.delt),
path("edt",views.edt),
]
