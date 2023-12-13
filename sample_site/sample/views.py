from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import EmployeeRoster

# Create your views here.
# def home(request):
#     template = loader.get_template("myhome.html")
#     return HttpResponse(template.render())

# Members view
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
def engWorksheet1(request):
    template = loader.get_template("eng/01-worksheet.html")
    return HttpResponse(template.render())

# English Worksheet 13 view
def engWorksheet13(request):
    template = loader.get_template("eng/13-worksheet.html")
    return HttpResponse(template.render())

# Main view for landing page or home page
def main(request):
    template = loader.get_template("main.html")
    return HttpResponse(template.render())

# Sample view
def sample(request):
    template = loader.get_template("sample.html")
    return HttpResponse(template.render())

# English Grammar view
def engGrammar(request):
    template = loader.get_template("eng/grammar.html")
    return HttpResponse(template.render())

# Home Science Orange Squash
def OrangeSquash(request):
    template = loader.get_template("hs/orange-squash.html")
    return HttpResponse(template.render())