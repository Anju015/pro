from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
# # Create your views here.
# from . models import reg_tbl

def home(request):
   return render(request,'supplier_home.html')