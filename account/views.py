from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm, ForgetForm
from django.contrib.auth import login, authenticate, logout
from core.models import User, Address
from django.utils.translation import gettext_lazy as _


def login_user(request):
    if request.user.is_authenticated:
        return redirect('/')

    login_form = LoginForm(request.POST or None)
    if login_form.is_valid():
        phone = login_form.cleaned_data.get('phone')
        password = login_form.cleaned_data.get('password')
        user = authenticate(request, phone=phone, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            login_form.add_error('phone', _('کاربری با مشخصات وارد شده وجود ندارد!'))

    context = {
        'login_form': login_form
    }
    return render(request, 'account/login.html', context)


def register(request):
    if request.user.is_authenticated:
        return redirect('/')
    register_form = RegisterForm(request.POST or None)

    if register_form.is_valid():
        phone = register_form.cleaned_data.get('phone')
        password = register_form.cleaned_data.get('password')
        email = register_form.cleaned_data.get('email')
        User.objects.create_user(phone=phone, email=email, password=password)
        return redirect('login')

    context = {
        'register_form': register_form
    }
    return render(request, 'account/register.html', context)


def log_out(request):
    logout(request)
    return redirect('login')


def forget_password(request):
    forget_form = ForgetForm(request.POST or None)
    if forget_form.is_valid():
        phone = forget_form.cleaned_data.get('phone')
        email = forget_form.cleaned_data.get('email')
        user = User.objects.filter(phone=phone, email=email)
        if user:
            # send mail
            print(f"Sendig mail! for {user[0].phone}")
        else:
            forget_form.add_error('phone', _('کاربری با مشخصات وارد شده وجود ندارد!'))

    context = {
        'forget_form': forget_form
    }
    return render(request, "account/forget_password.html", context)


@login_required(login_url='/account/login')
def profile(request):
    return render(request, 'account/profile.html', {"user": request.user})


@login_required(login_url='/account/login')
def address(request):
    return render(request, 'account/address.html', {"addresses": Address.objects.filter(owner=request.user)})