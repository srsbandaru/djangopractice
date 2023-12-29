from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name = "main"),
    path('members/', views.home, name = "home"),
    path('members/details/<int:id>', views.details, name = "details"),
    path("sample/", views.sample, name = "sample"),
    path('eng/worksheet-1', views.engWorksheet1, name = "engWorksheet1"),
    path('eng/worksheet-13', views.engWorksheet13, name = "engWorksheet13"),
    path('eng/grammar', views.engGrammar, name = "engGrammar"),
    path('hs/orange-squash', views.OrangeSquash, name = "OrangeSquash"),
    path('bc/revision', views.revision, name = "revision"),
    path('painting/exam-QA', views.exam, name = "exam"),
    path('students/', views.students, name = "students"),
    path('students/details/<int:id>', views.studentDetails, name = "studentDetails"),
    path('employee/', views.employee, name = "employee")
]