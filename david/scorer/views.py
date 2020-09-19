from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth, Group
from django.template.response import TemplateResponse
from django.urls import reverse
from .models import *
from django.http import *
from django.views import View

def landing_page(request, template_name='login.html'):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

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
                    teacher= Teacher.objects.get(mail=username)
                    teacherMail = teacher.mail
                    return teacher_main(request,teacherMail)
        
        else:
            args3 = {}
            args3['errorStatement'] = "Invalid Login Credentials. Please Try Again"
            return render(request, template_name, args3)

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

def teacher_main(request, teacherMail, template_name='Teacher1.html'):
    args2 = {}
    teacherObj = Teacher.objects.filter(mail=teacherMail)
    teacherObj = teacherObj[0]
    args2['teacherName'] = teacherObj.fName + " " + teacherObj.lName
    args2['subjectName'] = teacherObj.subject
    args2['mail'] = teacherObj.mail
    return render(request, template_name, args2)

def teacher_create(request, teacherMail, template_name='CreateTeach.html'):
    return render(request, template_name, {'mail': teacherMail})

def teacher_list(request):
    args={}
    stuobj = Student.objects.all()
    args['stus']=stuobj
    return render(request, 'ListTeach.html',args)
    

def teacher_view(request, year, rollNo, template_name='TeacherStudentDetail.html'):
    studentObj = Student.objects.filter(rollNo = rollNo, year=year)
    studentObj = studentObj[0]
    context = {}
    context['studentName'] = studentObj.fName + " " + studentObj.lName
    context['rollNo'] = studentObj.rollNo
    context['year'] = studentObj.year
    context['branchName'] = studentObj.branch
    context['dmMarks'] = studentObj.DMgrade
    context['dcMarks'] = studentObj.DCgrade
    context['coaMarks'] = studentObj.COAgrade
    context['seMarks'] = studentObj.SEgrade
    context['pasMarks'] = studentObj.PaSgrade
    context['dsMarks'] = studentObj.DSgrade
    
    return render(request, template_name, context)

class teacher_detail(View):
    def get(self, request):
        return render(request, 'DetailTeach.html')

    def post(self, request):
        rollNo = request.POST.get('rollNo')
        rollNo = int(rollNo)
        year = request.POST.get('year')
        year = int(year)
        return teacher_view(request, year, rollNo)

