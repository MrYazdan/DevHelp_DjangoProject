from django.db import models
from django.utils.translation import gettext_lazy as _
from thumbnails.fields import ImageField
from core.models import LogicalModel, TimeStampMixin
from core.utils import Controllers


class MultiImages(LogicalModel, TimeStampMixin):
    name = models.CharField(max_length=60, verbose_name=_('Album Name'),
                            help_text=_("This is album name (for hint to select true album)"))

    class Meta:
        verbose_name = _("Image Album")
        verbose_name_plural = _("Albums")

    def default(self):
        return self.image_set.filter(default=True).first().image.url if self.image_set.filter(default=True) else \
            self.image_set.all().first().image.url

    def __str__(self):
        return self.name


class Image(LogicalModel, TimeStampMixin):
    image = ImageField(upload_to=Controllers.Image.img_renamer, verbose_name=_("Image Field"),
                       help_text=_("This is image of image field"))
    default = models.BooleanField(default=False, verbose_name=_("Default"),
                                  help_text=_("This is default field for images"))
    rel = models.ForeignKey(to=MultiImages, on_delete=models.CASCADE, verbose_name=_('Album relation'),
                            help_text=_("This is album relation for set image to this"))

    class Meta:
        verbose_name = _("Image")
        verbose_name_plural = _("Images")

    def __str__(self):
        return super().__str__()
