from django.shortcuts import render
import os
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views import generic
from django.views.generic.base import View
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

from .forms import UserForm


# Create your views here.
def home(request):
    return render(request, 'home.html', {})


class UserFormView(View):
    form_class = UserForm
    template_name = 'register.html'

    # display blank form
    # def __init__(self, **kwargs):
    #     super().__init__(kwargs)
    #     self.POST = None

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # process form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit=False)  # here we have just stored it locally, not to the db yet

            # cleaned (normalized) data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            # returns User objects if credentials are correct
            user = authenticate(username=username, password=password)

            if user is not None:

                if user.is_active:
                    login(request, user)
                    return redirect('home')

        return render(request, self.template_name, {'form': form})


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        group = None
        if user is not None:
            if user.is_active:
                login(request, user)
                if request.user.groups.exists():
                    group = request.user.groups.all()[0].name

                    if group == 'prodigy':
                        return render(request, 'prodigy.html', {})

                    if group == 'faculty':
                        return render(request, 'faculty.html', {})

                else:
                    return render(request, 'home.html', {})
            else:
                return render(request, 'login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'login.html', {'error_message': 'Invalid login'})
    return render(request, 'login.html')


def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    return render(request, 'login.html', {'form': form})
