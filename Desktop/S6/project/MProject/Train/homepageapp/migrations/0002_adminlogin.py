# Generated by Django 3.2 on 2021-06-04 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepageapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='adminlogin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]
