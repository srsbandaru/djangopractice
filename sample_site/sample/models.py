from django.db import models

# Create your models here.
class EmployeeRoster(models.Model):
    fName = models.CharField(max_length=255)
    lName = models.CharField(max_length=255)
    Department = models.CharField(max_length=255)
    Supervisor = models.CharField(max_length=255)
    emailAddress = models.EmailField(null=True)