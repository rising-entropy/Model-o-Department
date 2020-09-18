from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth, Group
from django.template.response import TemplateResponse
from .models import *
from django.http import *

def landing_page(request, template_name='login.html'):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            query_set = Group.objects.filter(user = user)
            for g in query_set:
                if g.name == 'Student':
                    #user ka year n rollNo lena hain
                    studentData = Student.objects.get(mail=username)
                    rollNo = studentData.rollNo
                    year = studentData.year
                    return student_page(request, year, rollNo)
                else:
                    return teacher_main(request)
        
        else:
            args = {}
            args['errorStatement'] = "Invalid Login Credentials. Please Try Again"
            return render(request, template_name, args)

    else:
        return render(request,'login.html')

def student_page(request, year, rollNo, template_name='student1.html'):
    args2 = {}
    studentObj = Student.objects.filter(rollNo = rollNo, year=year)
    studentObj = studentObj[0]
    args2['studentName'] = studentObj.fName + " " + studentObj.lName
    args2['rollNo'] = studentObj.rollNo
    args2['branchName'] = studentObj.branch
    args2['dmMarks'] = studentObj.DMgrade
    args2['dcMarks'] = studentObj.DCgrade
    args2['coaMarks'] = studentObj.COAgrade
    args2['seMarks'] = studentObj.SEgrade
    args2['pasMarks'] = studentObj.PaSgrade
    args2['dsMarks'] = studentObj.DSgrade
    
    return render(request, template_name, args2)

def teacher_main(request):
    return render(request, 'Teacher1.html')

def teacher_create(request):
    return render(request, 'CreateTeach.html')

def teacher_list(request):
    return render(request, 'ListTeach.html')

def teacher_detail(request, year, rollNo):
    return render(request, 'DetailTeach.html')
