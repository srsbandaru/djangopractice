from django.contrib import admin
from .models import EmployeeRoster
from .models import Students

# Register your models here.
class EmployeeRosterAdmin(admin.ModelAdmin):
    list_display = ("fName", "lName", "emailAddress", "Department", "Supervisor")

admin.site.register(EmployeeRoster, EmployeeRosterAdmin)

class studentAdmin(admin.ModelAdmin):
    list_display = ("studentName", "studentAge", "studentEducation")

admin.site.register(Students, studentAdmin)
