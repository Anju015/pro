# Generated by Django 3.2 on 2021-05-06 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GUE_Customer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='cust_reg_tbl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('contact', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('uname', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]
