from django.contrib.auth.models import AbstractUser, UserManager
from django.core import validators
from django.core.validators import MinLengthValidator
from django.db import models
from django_jalali.db import models as jmodels
from django.utils.translation import gettext_lazy as _


# BaseManager :
class BaseManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)

    # define method for access all querysets
    def get_archive(self):
        return super().get_queryset()

    # define deleted item for easy access data
    def get_deleted_list(self):
        return super().get_queryset().filter(is_deleted=True)

    # define deactive profile item
    def get_deactive_list(self):
        return self.get_queryset().filter(is_active=False)


# Logical Model :
class LogicalModel(models.Model):
    is_deleted = models.BooleanField(
        default=False,
        verbose_name=_("Deleted status"),
        help_text=_("This is deleted status")
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name=_("Active status"),
        help_text=_("This is active status")
    )

    objects = BaseManager()

    class Meta:
        abstract = True

    def deleter(self):
        self.is_deleted = True
        self.save()

    def deactive(self):
        self.is_active = False
        self.save()


class TimeStampMixin(models.Model):
    create_time = jmodels.jDateTimeField(
        auto_now_add=True,
        verbose_name=_("Created time"),
        help_text=_("This is created time")
    )
    modify_time = jmodels.jDateTimeField(
        auto_now=True,
        verbose_name=_("Modified time"),
        help_text=_("This is modified time")
    )

    class Meta:
        abstract = True


class CustomUserManager(UserManager):

    def create_superuser(self, username=None, email=None, password=None, **extra_fields):
        username = extra_fields['phone']
        return super().create_superuser(username, email, password, **extra_fields)

    def create_user(self, username=None, email=None, password=None, **extra_fields):
        username = extra_fields['phone']
        return super().create_user(username, email, password, **extra_fields)


class User(AbstractUser):
    USERNAME_FIELD = 'phone'

    phone = models.CharField(max_length=11, unique=True, validators=[
        validators.RegexValidator(regex='^(\+98|0)?9\d{9}$',
                                  message=_("Phone number must be entered in the true IR (iran) format."),
                                  code=_('invalid IR phone number'))
    ])
    ncode = models.CharField(max_length=10, validators=[
        MinLengthValidator(10),

    ], unique=True, null=True, blank=True)

    objects = CustomUserManager()


class Address(LogicalModel):
    owner = models.ForeignKey(to="User", on_delete=models.CASCADE)
    lat = models.FloatField(null=True, blank=True, default=None)
    lng = models.FloatField(null=True, blank=True, default=None)
    country = models.CharField(max_length=120)
    city = models.CharField(max_length=120)
    address = models.TextField()
    postal_code = models.CharField(max_length=10)
    no = models.PositiveIntegerField()

    def __str__(self):
        return self.address
