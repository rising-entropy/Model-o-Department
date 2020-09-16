from django.shortcuts import render

def landing_page(request):
    return render(request,'login.html')

def student_page(request):
    return render(request,'student1.html')