
from django.contrib import admin
from django.urls import path
from cmsapp.views import home, dept, adddept, removedept, student, addstudent, removestudent

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", home, name="home"),
    path("dept", dept, name="dept"),
    path("adddept", adddept, name="adddept"),
    path("removedept/<int:id>", removedept, name="removedept"),
    path("student", student, name="student"),
    path("addstudent", addstudent, name="addstudent"),
    path("removestudent/<int:id>", removestudent, name="removestudent"),
    
    
]
