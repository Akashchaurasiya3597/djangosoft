from django.contrib import admin

from .models import StudentDatabase, EmployeeDatabase, CustomerDatabase
class AdminEmployee(admin.ModelAdmin):
    list_display = ['Name', 'Mobile', 'Email', 'Salary']


class AdminCustomer(admin.ModelAdmin):
    list_display = ['Name', 'Mobile', 'Email', 'Sales']
class AdminStudent(admin.ModelAdmin):
    list_display = ['Name', 'Mobile', 'Email', 'Marks']

admin.site.register(EmployeeDatabase, AdminEmployee)
admin.site.register(CustomerDatabase, AdminCustomer)
admin.site.register(StudentDatabase, AdminStudent)
