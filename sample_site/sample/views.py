from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import EmployeeRoster

# Create your views here.
# def home(request):
#     template = loader.get_template("myhome.html")
#     return HttpResponse(template.render())

# Home view
def home(request):
    myEmployees = EmployeeRoster.objects.all().values()
    template = loader.get_template("myhome.html")
    context = {
        "Employees":myEmployees
    }
    return HttpResponse(template.render(context, request))

# Member Details view
def details(request, id):
    myEmployee = EmployeeRoster.objects.get(id=id)
    template = loader.get_template("member_details.html")
    context = {
        "member":myEmployee
    }
    return HttpResponse(template.render(context, request))

# English Worksheet 1 view
def worksheet1(request):
    template = loader.get_template("eng/01-worksheet.html")
    return HttpResponse(template.render())