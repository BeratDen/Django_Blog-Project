from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate
# Create your views here.


def register(request):

    form = RegisterForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')

        newUser = User(username=username)
        newUser.set_password(password)
        newUser.save()

        auth_login(request, newUser)
        messages.success(request, "Başarıyla Kayıt Oldunuz.")
        return redirect("index")
    else:
        form = RegisterForm()
        # TODO: form not raising error
        print(form.errors)
        context = {
            'form': form
        }
        return render(request, 'users/register.html', context=context)


def login(request):
    form = LoginForm(request.POST or None)

    context = {
        'form': form
    }

    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')

        user = authenticate(username=username, password=password)

        if user is None:
            messages.error(request, "Kullanıcı Adı veya Şifre Yanlış")
            return render(request, "users/login.html", context=context)

        messages.success(request, "Başarıyla Giriş Yaptınız.")
        auth_login(request, user)
        return redirect("index")

    return render(request, "users/login.html", context=context)

    return render(request, 'users/login.html')


def logout(request):
    pass
