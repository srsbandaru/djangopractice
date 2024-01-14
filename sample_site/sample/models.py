from django.db import models

# Create your models here.
class EmployeeRoster(models.Model):
    fName = models.CharField(max_length=255)
    lName = models.CharField(max_length=255)
    Department = models.CharField(max_length=255)
    Supervisor = models.CharField(max_length=255)
    emailAddress = models.EmailField(null=True)

    def __str__(self):
        return f"{self.fName} {self.lName}"

# Students model 
class Students(models.Model):
    studentName = models.CharField(max_length=255)
    studentAge = models.IntegerField(null=True)
    studentEducation = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.studentName}"

# Employee model
class Employee(models.Model):
    EMPLOYEE_ID = models.IntegerField(null=True)
    FIRST_NAME = models.CharField(max_length=255)
    LAST_NAME = models.CharField(max_length=255)
    JOB_ID = models.CharField(max_length=255)
    SALARY = models.IntegerField(null=True)
# Trip model
class Trip(models.Model):
    Days = models.CharField(max_length=255)
    Origin = models.CharField(max_length=255)
    Destination = models.CharField(max_length=255)

