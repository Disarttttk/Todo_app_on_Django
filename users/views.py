from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from main.models import ToDoNote

from .models import User


def login(request):

    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            session_key = request.session.session_key
            if user:
                auth.login(request, user)
                if session_key:
                    ToDoNote.objects.filter(session_key=session_key).update(user=user)
                return redirect('main:index')


    else:
        form = UserLoginForm()

    context = {
        'title': 'Авторизация',
        'form': form,
    }
    return render(request, template_name='users/login.html', context=context)


def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = form.instance
            session_key = request.session.session_key
            auth.login(request, user)
            if session_key:
                ToDoNote.objects.filter(session_key=session_key).update(user=user)
            return redirect('main:index')
    else:
        form = UserRegistrationForm()

    context = {
        'title': 'Регистрация',
        'form': form
    }
    return render(request=request, template_name='users/registration.html', context=context)


@login_required
def profile(request):
    user = request.user

    if request.method == 'POST':
        form = UserProfileForm(data=request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user:profile')

    form = UserProfileForm(instance=user)
    context = {
        'form': form
    }
    return render(request=request, template_name='users/profile.html', context=context)


@login_required
def logout(request):
    auth.logout(request)
    return redirect('main:index')
