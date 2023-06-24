from random import choices

from django.db import models
# Create your models here.

class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    about = models.TextField()
    types = models.CharField(max_length=100,choices=
                            (('IT','IT'),
                             ('NON IT','NON IT'),
                             ('MOBILE PHONE','MOBILE PHONE'),
                             ('new', 'new'),
                             ))
    added_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

#Employee model
class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.TextField()
    phone = models.IntegerField()
    about = models.TextField()
    position = models.CharField(max_length=100,choices=(
        ('manager', 'manager'),
        ('software developer','sd'),
        ('project leader','pl')
    ))
    company = models.ForeignKey(Company,on_delete=models.CASCADE)