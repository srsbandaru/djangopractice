from django.urls import path
from . import views

app_name = "sample"

urlpatterns = [
    path('', views.main, name = "main"),
    path('members/', views.home, name = "home"),
    path('members/details/<int:id>', views.details, name = "details"),
    path("sample/", views.sample, name = "sample"),
    path('eng/worksheet-1', views.engWorksheet1, name = "engWorksheet1"),
    path('eng/worksheet-13', views.engWorksheet13, name = "engWorksheet13"),
    path('eng/worksheet-16', views.engWorksheet16, name = "engWorksheet16"),
    path('eng/worksheet-18', views.engWorksheet18, name = "engWorksheet18"),
    path('eng/grammar', views.engGrammar, name = "engGrammar"),
    path('hs/orange-squash', views.OrangeSquash, name = "OrangeSquash"),
    path('bc/revision', views.revision, name = "revision"),
    path('painting/exam-QA', views.exam, name = "exam"),
    path('students/', views.students, name = "students"),
    path('students/details/<int:id>', views.studentDetails, name = "studentDetails"),
    path('students/create', views.create_student.as_view(), name = "create_student"),
    path('employee/', views.employee, name = "employee"),
    path('employee/details/<int:id>', views.employeeDetails, name = "employeeDetails"),
    path('employee/create', views.create_employee.as_view(), name = "create_employee"),
    path('travelblog/travel', views.travelBlog, name = "travelBlog"),
    path('trip/', views.TripView, name = "TripView"),
    path('trip/details/<int:id>', views.TripDetails, name = "TripDetails"),
    path('festivals/sankranthi', views.Sankranthi, name = "Sankranthi"),
]