from django.db import models

# Create your models here.


class Tenant(models.Model):
    f_name = models.CharField(max_length=20)
    l_name = models.CharField(max_length=25)
    u_name = models.CharField(max_length=20)
    password = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    account = models.IntegerField()
    move_in_date = models.DateField(auto_now=False, auto_now_add=False)
    move_out_date = models.DateField(auto_now=False)
    email = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    unit = models.ForeignKey('Unit', on_delete=models.CASCADE)


class Unit(models.Model):
    address = models.CharField(max_length=100)
    sqft = models.IntegerField()
    num_bed = models.IntegerField()
    num_bath = models.FloatField()
    max_res = models.IntegerField()
    available = models.BooleanField(default=True)

