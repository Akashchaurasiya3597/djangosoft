from django.contrib import admin

from .models import StudentDatabase, EmployeeDatabase, CustomerDatabase
class AdminEmployee(admin.ModelAdmin):
    list_display = ['EName', 'Salary']


class AdminCustomer(admin.ModelAdmin):
    list_display = ['CName', 'Sales']
class AdminStudent(admin.ModelAdmin):
    list_display = ['SName', 'Marks']

admin.site.register(EmployeeDatabase, AdminEmployee)
admin.site.register(CustomerDatabase, AdminCustomer)
admin.site.register(StudentDatabase, AdminStudent)
