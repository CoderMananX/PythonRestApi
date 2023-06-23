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

    #Employee modelsd