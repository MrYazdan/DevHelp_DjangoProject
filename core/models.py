from django.db import models


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


# BaseModel :
class BaseModel(BaseManager):

    # usually columns
    create_time = models.DateTimeField(auto_now_add=True)
    modify_time = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    # initilize manager
    objects = BaseManager()

    class Meta:
        abstract = True
