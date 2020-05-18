from django.contrib import admin
from .models import CompanyData, PersonData

class AdminCompany(admin.ModelAdmin):
    list_display = ['Company_Name', 'Company_Email', 'Company_Number', 'Company_Website']
class Adminperson(admin.ModelAdmin):
    list_display = ['First_Name', 'Last_Name', 'Age', 'Email','Mobile_Number']

admin.site.register(CompanyData,AdminCompany)
admin.site.register(PersonData,Adminperson)
