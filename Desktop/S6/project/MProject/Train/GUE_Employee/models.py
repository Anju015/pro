from django.db import models


# #employee registration..........

class emp_reg_tbl(models.Model):
    empname=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    age=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    dept=models.CharField(max_length=100)
    dtime=models.DateField(max_length=100)
    uname=models.CharField(max_length=100)
    passwd=models.CharField(max_length=100)
    vrf = models.CharField(max_length=100)

class pdt_req_tbl(models.Model):
    pdtname=models.CharField(max_length=100)
    qty=models.DecimalField(max_digits=5,decimal_places=2)
    supname=models.CharField(max_length=100)

#class leave_tbl(models.Model):
 #   empid=models.ForeignKey("emp_reg_tbl",on_delete=models.CASCADE)
 #   subject=models.CharField(max_length=100)
 #   leave_date=models.DateTime(max_length=100)
  #  cur_date=models.DateField(max_length=100)
