from django.contrib import admin
from .models import EmployeeRoster
from .models import Students
from .models import Trip
from .models import Employee

# Register your models here.
class EmployeeRosterAdmin(admin.ModelAdmin):
    list_display = ("fName", "lName", "emailAddress", "Department", "Supervisor")

admin.site.register(EmployeeRoster, EmployeeRosterAdmin)

class studentAdmin(admin.ModelAdmin):
    list_display = ("studentName", "studentAge", "studentEducation")

admin.site.register(Students, studentAdmin)

class employeeAdmin(admin.ModelAdmin):
    list_display = ("FIRST_NAME", "LAST_NAME", "JOB_ID", "SALARY", "EMPLOYEE_ID")

admin.site.register(Employee, employeeAdmin)

class tripAdmin(admin.ModelAdmin):
    list_display = ("Days", "Origin", "Destination")

admin.site.register(Trip, tripAdmin) 

