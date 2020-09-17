from django.shortcuts import render

def landing_page(request):
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
