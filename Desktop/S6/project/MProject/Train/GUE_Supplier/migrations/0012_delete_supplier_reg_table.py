# Generated by Django 3.2 on 2021-05-30 15:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('GUE_Supplier', '0011_rename_s_reg_table_supplier_reg_table'),
    ]

    operations = [
        migrations.DeleteModel(
            name='supplier_reg_table',
        ),
    ]
