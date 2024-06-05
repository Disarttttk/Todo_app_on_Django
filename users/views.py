from django.contrib import auth
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import UserLoginForm


def login(request):

    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return redirect('main:index')

    else:
        form = UserLoginForm()

    context = {
        'form': form,
    }
    return render(request, template_name='users/login.html', context=context)