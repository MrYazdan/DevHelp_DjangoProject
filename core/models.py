from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.utils.translation import gettext_lazy as _


# BaseManager :
class BaseManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False, is_active=True)

    # define method for access all querysets
    def get_archive(self):
        return super().get_queryset()

    # define deleted item for easy access data
    def get_deleted_list(self):
        return super().get_queryset().filter(is_deleted=True)

    # define active profile item
    def get_active_list(self):
        return self.get_queryset().filter(is_active=True)

    # define deactive profile item
    def get_deactive_list(self):
        return self.get_queryset().filter(is_active=False)


# BaseModel :
class BaseModel(models.Model):
    # usually columns
    create_time = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("Created time"),
        help_text=_("This is created time")
    )
    modify_time = models.DateTimeField(
        auto_now=True,
        verbose_name=_("Modified time"),
        help_text=_("This is modified time")
    )
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

    # initilize manager
    objects = BaseManager()

    class Meta:
        abstract = True


class CustomUserManager(UserManager):

    def create_superuser(self, username=None, email=None, password=None, **extra_fields):
        username = extra_fields['phone']
        return super().create_superuser(username, email, password, **extra_fields)


class User(AbstractUser):
    USERNAME_FIELD = 'phone'

    phone = models.CharField(max_length=11, unique=True)

    objects = CustomUserManager()


class Address(models.Model):
    owner = models.ForeignKey(to="User", on_delete=models.CASCADE)
    lat = models.FloatField(null=True, blank=True)
    lng = models.FloatField(null=True, blank=True)
    country = models.CharField(max_length=120)
    city = models.CharField(max_length=120)
    address = models.TextField()
    postal_code = models.CharField(max_length=10)
    no = models.PositiveIntegerField()
