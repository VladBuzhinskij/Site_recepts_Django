from django.shortcuts import render
from userss.forms import UserLoginForm,UserRegistrationForm,ProfileForm
from django.contrib import auth,messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

def Login(request):
    if request.method=='POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username=request.POST['username']
            password=request.POST['password']
            user = auth.authenticate(username=username,password=password)
            if user:
                auth.login(request,user)
                messages.success(request,"Вход выполнен")
                return HttpResponseRedirect(reverse('main:index'))  
    else:
        form=UserLoginForm()
    context={
        'title':'Авторизация',
        'form':form
    }
    return render(request, 'userss/login.html', context)

@login_required
def Registration(request):
    if request.method=='POST':
        form = UserRegistrationForm(data=request.POST)
        print('1')
        if form.is_valid():
            form.save()
            user=form.instance
            auth.login(request,user)
            messages.success(request,"Регистрация и вход выполнены")
            return HttpResponseRedirect(reverse('main:index'))  
    else:
        form=UserRegistrationForm()
    
    context={
        'title':'Регистрация',
        'form':form
    }
    return render(request, 'userss/registration.html', context)

@login_required
def Profile(request):
    if request.method=='POST':
        form = ProfileForm(data=request.POST, instance=request.user)
        print('1')
        if form.is_valid():
            form.save()
            messages.success(request,"Даные сохранены")
            return HttpResponseRedirect(reverse('user:profile'))  
    else:
        form=ProfileForm(instance=request.user)
    
    context={
        'title':'Профиль',
        'form':form
    }
    return render(request, 'userss/profile.html', context)

def logout(request):
    auth.logout(request)
    messages.success(request,"Выход выплонен")
    return HttpResponseRedirect(reverse('main:index'))
