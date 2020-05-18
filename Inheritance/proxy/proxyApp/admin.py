from django.contrib import admin

from .models import EmployeeDatabase,ProxyDatabase
class AdminEmployee(admin.ModelAdmin):
    list_display = ['Name', 'Mobile', 'Email', 'Salary']
class AdminProxy(admin.ModelAdmin):
    list_display = ['Name', 'Mobile', 'Email', 'Salary']


admin.site.register(ProxyDatabase,AdminProxy)
admin.site.register(EmployeeDatabase, AdminEmployee)
