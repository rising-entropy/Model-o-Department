from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth, Group
from django.template.response import TemplateResponse

def landing_page(request, template_name='login.html'):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            query_set = Group.objects.filter(user = user)
            for g in query_set:
                if g.name == 'Student':
                    return render(request, 'student1.html')
                else:
                    return render(request, 'Teacher1.html')
        
        else:
            args = {}
            args['errorStatement'] = "Invalid Login Credentials. Please Try Again"
            return render(request, template_name, args)

    else:
        return render(request,'login.html')

def student_page(request, year, rollNo):
    return render(request,'student1.html')

def teacher_main(request):
    return render(request, 'Teacher1.html')

def teacher_create(request):
    return render(request, 'CreateTeach.html')

def teacher_list(request):
    return render(request, 'ListTeach.html')

def teacher_detail(request, year, rollNo):
    return render(request, 'DetailTeach.html')
