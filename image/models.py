from django.db import models
from django.utils.translation import gettext_lazy as _
from thumbnails.fields import ImageField
from core.models import LogicalModel, TimeStampMixin
from core.utils import Controllers


class MultiImages(LogicalModel, TimeStampMixin):
    def default(self):
        return self.images.filter(default=True).first()


class Image(LogicalModel, TimeStampMixin):
    image = ImageField(upload_to=Controllers.Image.img_renamer,
                       verbose_name=_("Image Field"),
                       help_text=_("This is image of image field"))
    default = models.BooleanField(default=False,
                                  verbose_name=_("Default"),
                                  help_text=_("This is default field for images"))
    relation = models.ForeignKey(MultiImages, related_name='images', on_delete=models.CASCADE)
