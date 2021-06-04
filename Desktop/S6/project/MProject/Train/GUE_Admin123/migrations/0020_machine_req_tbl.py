# Generated by Django 3.2 on 2021-05-31 06:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('GUE_Employee', '0008_emp_reg_tbl'),
        ('GUE_Admin123', '0019_cat_reg_tbl'),
    ]

    operations = [
        migrations.CreateModel(
            name='machine_req_tbl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('machinename', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=100)),
                ('empname', models.CharField(max_length=100)),
                ('empid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GUE_Employee.emp_reg_tbl')),
            ],
        ),
    ]
