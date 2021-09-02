from django.utils.translation import gettext_lazy as _
from django.db import models
from core.models import TimeStampMixin, LogicalModel, User, BaseManager
from products.models import Product


class CommentManager(BaseManager):

    def get_queryset(self):
        return super().get_queryset().filter(is_accept=True)


class Comment(LogicalModel, TimeStampMixin):
    is_accept = models.BooleanField(default=False, auto_created=True)
    fullname = models.CharField(max_length=60, verbose_name=_("Comment Writer Fullname"),
                                help_text=_("This is fullname of comment writer"))
    email = models.EmailField(_('email address'))
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name=_("Product"),
                                help_text=_("This is product for set comment for this"))
    reply = models.ForeignKey('Comment', null=True, blank=True, on_delete=models.SET_NULL, verbose_name=_("Reply"),
                              help_text=_("This is reply for this commnet"), related_name="replies")
    message = models.TextField(max_length=1000, verbose_name=_("Comment Message"),
                               help_text=_("This is comment message"))

    objects = CommentManager()

    class Meta:
        verbose_name = _("Comment")
        verbose_name_plural = _("Comments")

    def accept(self):
        self.is_accept = True
        self.save()
        return self.is_accept

    def __str__(self):
        return f"{self.fullname}:{self.email}"
