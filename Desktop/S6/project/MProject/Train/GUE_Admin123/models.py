from django.db import models
#from GUE_Employee.models import emp_reg_tbl
# Create your models here.

# Product registration
class pdt_reg_tbl(models.Model):
    pdtname=models.CharField(max_length=100)
    pdtimage=models.CharField(max_length=100)
    pdtprice = models.CharField(max_length=100)
    pdttax=models.CharField(max_length=100)
    pdtquality=models.CharField(max_length=100)
    pdtstatus=models.CharField(max_length=100)
    category = models.CharField(max_length=100)

# supplier registration
class sup_reg_tbl(models.Model):
    supname=models.CharField(max_length=100)
    contact=models.CharField(max_length=100)
    company = models.CharField(max_length=100)

#Stock add
class stocks(models.Model):
    productid = models.ForeignKey("pdt_reg_tbl", on_delete=models.CASCADE)
    stock = models.CharField(max_length=100)


#category add
class cat_reg_tbl(models.Model):
    pdtcatname = models.CharField(max_length=100)
    pdtcatstatus = models.CharField(max_length=100)

#machine request
class machine_req_tbl(models.Model):
    machinename=models.CharField(max_length=100)
    status=models.CharField(max_length=100)
    empid=models.ForeignKey("GUE_Employee.emp_reg_tbl",on_delete=models.CASCADE)
    empname=models.CharField(max_length=100)


