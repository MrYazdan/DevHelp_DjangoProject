from django import forms
from core.models import User
from django.core import validators
from django.utils.translation import gettext_lazy as _


class LoginForm(forms.Form):
    phone = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': _("لطفا شماره همراه خود را وارد نمایید"),
                                      'class': "block w-full py-4 rounded-md px-3 bg-black bg-opacity-30 mb-4"}),
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': _('لطفا کلمه عبور خود را وارد نمایید'),
                                          'class': "block w-full py-4 rounded-md px-3 bg-black bg-opacity-30 mb-4"}),
    )

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        is_exists_user = User.objects.filter(phone=phone).exists()
        if not is_exists_user:
            raise forms.ValidationError(_('کاربری با مشخصات وارد شده ثبت نام نکرده است'))

        return phone


class RegisterForm(forms.Form):
    phone = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'لطفا شماره تماس خود را وارد نمایید',
                                      'class': "block w-full py-4 rounded-md px-3 bg-black bg-opacity-30 mb-4"}),
        validators=[
            validators.MaxLengthValidator(limit_value=11,
                                          message=_('تعداد کاراکترهای وارد شده نمیتواند بیشتر از 11 باشد')),
            validators.MinLengthValidator(8, _('تعداد کاراکترهای وارد شده نمیتواند کمتر از 8 باشد'))
        ]
    )

    email = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': _('لطفا ایمیل خود را وارد نمایید'),
                                      'class': "block w-full py-4 rounded-md px-3 bg-black bg-opacity-30 mb-4"}),
        validators=[
            validators.EmailValidator(_('ایمیل وارد شده معتبر نمیباشد'))
        ]
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': _('لطفا کلمه عبور خود را وارد نمایید'),
                                          'class': "block w-full py-4 rounded-md px-3 bg-black bg-opacity-30 mb-4"}),
    )

    re_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': _('لطفا تکرار کلمه عبور خود را وارد نمایید'),
                                          'class': "block w-full py-4 rounded-md px-3 bg-black bg-opacity-30 mb-4"}),
    )

    def clean_email(self):
        email = self.cleaned_data.get('email')
        is_exists_user_by_email = User.objects.filter(email=email).exists()
        if is_exists_user_by_email:
            raise forms.ValidationError(_('ایمیل وارد شده تکراری میباشد'))

        if len(email) > 40:
            raise forms.ValidationError(_('تعداد کاراکترهای ایمیل باید کمتر از 40 باشد'))

        return email

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        is_exists_user_by_phone = User.objects.filter(phone=phone).exists()

        if is_exists_user_by_phone:
            raise forms.ValidationError(_('این کاربر قبلا ثبت نام کرده است'))

        return phone

    def clean_re_password(self):
        password = self.cleaned_data.get('password')
        re_password = self.cleaned_data.get('re_password')
        print(password)
        print(re_password)

        if password != re_password:
            raise forms.ValidationError(_('کلمه های عبور مغایرت دارند'))

        return password
