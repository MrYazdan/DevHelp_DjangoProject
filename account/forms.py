from django import forms
from core.models import User
from django.core import validators
from django.utils.translation import gettext_lazy as _


class LoginForm(forms.Form):
    phone = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': _("Please enter your mobile number"),
                                      'class': "block w-full py-4 rounded-md px-3 bg-black bg-opacity-30 mb-4"}),
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': _('Please enter your password'),
                                          'class': "block w-full py-4 rounded-md px-3 bg-black bg-opacity-30 mb-4"}),
    )

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        is_exists_user = User.objects.filter(phone=phone).exists()
        if not is_exists_user:
            raise forms.ValidationError(_('There is no user with the entered profile!'))

        return phone


class ForgetForm(forms.Form):
    phone = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': _("Please enter your mobile number"),
                                      'class': "block w-full py-4 rounded-md px-3 bg-black bg-opacity-30 mb-4"}),
    )

    email = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': _('Please enter your email'),
                                      'class': "block w-full py-4 rounded-md px-3 bg-black bg-opacity-30 mb-4"}),
        validators=[
            validators.EmailValidator(_('The entered email is not valid'))
        ]
    )

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        is_exists_user = User.objects.filter(phone=phone).exists()
        if not is_exists_user:
            raise forms.ValidationError(_('There is no user with the entered contact number!'))
        return phone

    def clean_email(self):
        email = self.cleaned_data.get('email')
        is_exists_user_by_email = User.objects.filter(email=email).exists()
        if not is_exists_user_by_email:
            raise forms.ValidationError(_('The entered email is not valid'))

        if len(email) > 40:
            raise forms.ValidationError(_('Email characters must be less than 40'))

        return email


class RegisterForm(forms.Form):
    phone = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Please enter your contact number',
                                      'class': "block w-full py-4 rounded-md px-3 bg-black bg-opacity-30 mb-4"}),
        validators=[
            validators.MaxLengthValidator(limit_value=11,
                                          message=_('The number of characters entered can not be more than 11')),
            validators.MinLengthValidator(8, _('The number of characters entered can not be less than 8'))
        ]
    )

    email = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': _('Please enter your email'),
                                      'class': "block w-full py-4 rounded-md px-3 bg-black bg-opacity-30 mb-4"}),
        validators=[
            validators.EmailValidator(_('The entered email is not valid'))
        ]
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': _('Please enter your password'),
                                          'class': "block w-full py-4 rounded-md px-3 bg-black bg-opacity-30 mb-4"}),
    )

    re_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': _('Please enter your password again'),
                                          'class': "block w-full py-4 rounded-md px-3 bg-black bg-opacity-30 mb-4"}),
    )

    def clean_email(self):
        email = self.cleaned_data.get('email')
        is_exists_user_by_email = User.objects.filter(email=email).exists()
        if is_exists_user_by_email:
            raise forms.ValidationError(_('The entered email is duplicate'))

        if len(email) > 40:
            raise forms.ValidationError(_('Email characters must be less than 40'))

        return email

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        is_exists_user_by_phone = User.objects.filter(phone=phone).exists()

        if is_exists_user_by_phone:
            raise forms.ValidationError(_('This user has already registered'))

        return phone

    def clean_re_password(self):
        password = self.cleaned_data.get('password')
        re_password = self.cleaned_data.get('re_password')
        print(password)
        print(re_password)

        if password != re_password:
            raise forms.ValidationError(_('Passwords are different'))

        return password
