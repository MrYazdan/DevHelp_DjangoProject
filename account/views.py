from django.contrib.auth import mixins
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView
from order.models import Order
from products.models import OffCode
from .forms import LoginForm, RegisterForm, ForgetForm
from django.contrib.auth import login, authenticate
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


class Profile(mixins.LoginRequiredMixin, TemplateView):
    template_name = "account/profile.html"


class AddressView(mixins.LoginRequiredMixin, ListView):
    template_name = "account/address.html"

    def get_queryset(self):
        return Address.objects.filter(owner=self.request.user)


class UserOrders(mixins.LoginRequiredMixin, ListView):
    template_name = "account/paid.html"

    def get_queryset(self):
        return Order.objects.filter(payment_datetime__isnull=False)


class UserOffCodes(mixins.LoginRequiredMixin, ListView):
    template_name = "account/offcode.html"

    def get_queryset(self):
        return OffCode.objects.filter(for_users__username=self.request.user, active=True)