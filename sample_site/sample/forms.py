from django.forms import ModelForm
from sample.models import Students

class StudentForm(ModelForm):
    class Meta:
        model = Students
        fields = "__all__"
        
