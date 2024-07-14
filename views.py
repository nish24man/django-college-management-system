from django.shortcuts import render, redirect
from .forms import DeptForm, StudentForm
from .models import DeptModel, StudentModel

def home(request):
    return render(request, "home.html")

def dept(request):
    data = DeptModel.objects.all()
    return render(request, "dept.html", {"data": data})

def adddept(request):
    if request.method == "POST":
        data = DeptForm(request.POST)
        if data.is_valid():
            data.save()
            msg = "Department added successfully."
            fm = DeptForm()
            return render(request, "adddept.html", {"fm": fm, "msg": msg})
        else:
            msg = "Please correct the errors below."
            return render(request, "adddept.html", {"fm": data, "msg": msg})
    else:
        fm = DeptForm()
        return render(request, "adddept.html", {"fm": fm})

def removedept(request, id):
    de = DeptModel.objects.get(did=id)
    de.delete()
    return redirect("dept")

def student(request):
    data = StudentModel.objects.all()
    return render(request, "student.html", {"data": data})

def addstudent(request):
    if request.method == "POST":
        data = StudentForm(request.POST)
        if data.is_valid():
            data.save()
            msg = "Student added successfully."
            fm = StudentForm()
            return render(request, "addstudent.html", {"fm": fm, "msg": msg})
        else:
            msg = "Please correct the errors below."
            return render(request, "addstudent.html", {"fm": data, "msg": msg})
    else:
        fm = StudentForm()
        return render(request, "addstudent.html", {"fm": fm})

def removestudent(request, id):
    de = StudentModel.objects.get(rno=id)
    de.delete()
    return redirect("student")