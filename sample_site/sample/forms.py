from django.forms import ModelForm
from sample.models import Students
from sample.models import Employee

class StudentForm(ModelForm):
    class Meta:
        model = Students
        fields = "__all__"

class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"   
