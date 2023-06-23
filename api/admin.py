from django.contrib import admin
from .models import Company
# Register your models here.

class showCompany(admin.ModelAdmin):
    list_display = ["company_id","name","location","about","types","added_date","active"]
admin.site.register(Company,showCompany)