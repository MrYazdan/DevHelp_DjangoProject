from django import forms
from core.models import User
from django.core import validators
from django.utils.translation import gettext_lazy as _


class EditUserForm(forms.Form):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'لطفا نام خود را وارد نمایید', 'class': 'form-control'}),
    )

    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'لطفا نام خانوادگی خود را وارد نمایید', 'class': 'form-control'}),
    )


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
        widget=forms.TextInput(attrs={'placeholder': 'لطفا نام کاربری خود را وارد نمایید'}),
        label='نام کاربری',
        validators=[
            validators.MaxLengthValidator(limit_value=20,
                                          message='تعداد کاراکترهای وارد شده نمیتواند بیشتر از 20 باشد'),
            validators.MinLengthValidator(8, 'تعداد کاراکترهای وارد شده نمیتواند کمتر از 8 باشد')
        ]
    )

    email = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'لطفا ایمیل خود را وارد نمایید'}),
        label='ایمیل',
        validators=[
            validators.EmailValidator('ایمیل وارد شده معتبر نمیباشد')
        ]
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'لطفا کلمه عبور خود را وارد نمایید'}),
        label='کلمه ی عبور'
    )

    re_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'لطفا تکرار کلمه عبور خود را وارد نمایید'}),
        label='تکرار کلمه ی عبور'
    )

    def clean_email(self):
        email = self.cleaned_data.get('email')
        is_exists_user_by_email = User.objects.filter(email=email).exists()
        if is_exists_user_by_email:
            raise forms.ValidationError('ایمیل وارد شده تکراری میباشد')

        if len(email) > 20:
            raise forms.ValidationError('تعداد کاراکترهای ایمیل باید کمتر از 20 باشد')

        return email

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        is_exists_user_by_phone = User.objects.filter(phone=phone).exists()

        if is_exists_user_by_phone:
            raise forms.ValidationError('این کاربر قبلا ثبت نام کرده است')

        return phone

    def clean_re_password(self):
        password = self.cleaned_data.get('password')
        re_password = self.cleaned_data.get('re_password')
        print(password)
        print(re_password)

        if password != re_password:
            raise forms.ValidationError('کلمه های عبور مغایرت دارند')

        return password
