from django.db import models

# Create your models here.
class EmployeeRoster(models.Model):
    fName = models.CharField(max_length=255)
    lName = models.CharField(max_length=255)
    Department = models.CharField(max_length=255)
    Supervisor = models.CharField(max_length=255)
    emailAddress = models.EmailField(null=True)
# Students model 
class Students(models.Model):
    studentName = models.CharField(max_length=255)
    studentAge = models.IntegerField(null=True)
    studentEducation = models.CharField(max_length=255)
# Employee model
class Employee(models.Model):
    EMPLOYEE_ID = models.IntegerField(null=True)
    FIRST_NAME = models.CharField(max_length=255)
    LAST_NAME = models.CharField(max_length=255)
    JOB_ID = models.CharField(max_length=255)
    SALARY = models.IntegerField(null=True)