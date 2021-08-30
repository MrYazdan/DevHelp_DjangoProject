from django.core import validators
from django.db import models
from core.models import LogicalModel, User, TimeStampMixin
from django.utils.translation import gettext_lazy as _, get_language
from core.utils import Controllers


class SochialAccount(LogicalModel, TimeStampMixin):
    name_fa = models.CharField(
        max_length=60, verbose_name=_("Persian name"),
        help_text=_("This is persian name of sochial accounts")
    )
    name_en = models.CharField(
        max_length=60, verbose_name=_("English name"),
        help_text=_("This is english name of sochial accounts")
    )
    url = models.URLField(
        max_length=120, verbose_name=_("Link"),
        help_text=_("This is link of sochial accounts -> sample : 'https://instagram.com/myaccounts' ")
    )
    gb_ico = models.CharField(
        max_length=50, verbose_name=_("Icon"), validators=[
            validators.RegexValidator(regex='^(\+98|0)?9\d{9}$',
                                      message=_('GB Icon must be start with "gb_" and  end with alphabet char'),
                                      code=_('invalid gb ico'))
        ],
        help_text=_("This is icon of sochial accounts from gorbeh icon -> sample : 'gb_telegram' ")
    )

    class Meta:
        verbose_name = _("Sochial Account")
        verbose_name_plural = _("Sochial Accounts")

    @property
    def name(self):
        return self.name_en if get_language() == "en-US" else self.name_fa

    def __str__(self):
        return self.name


class Site(LogicalModel, TimeStampMixin):
    title_fa = models.CharField(max_length=90, verbose_name=_("Website Persian Title"),
                                help_text=_("This is persian website title"))
    title_en = models.CharField(max_length=90, verbose_name=_("Website English Title"),
                                help_text=_("This is english website title"))
    sub_title_fa = models.CharField(max_length=90, verbose_name=_("Website Persian Subtitle"),
                                    help_text=_("This is persian website subtitle"), null=True, default="", blank=True)
    sub_title_en = models.CharField(max_length=90, verbose_name=_("Website English Subtitle"),
                                    help_text=_("This is english website subtitle"), null=True, default="", blank=True)
    short_description_fa = models.CharField(max_length=360, blank=True, default="", null=True,
                                            verbose_name=_("Short Persian Description"),
                                            help_text=_("This is persian short description"))
    short_description_en = models.CharField(max_length=360, blank=True, default="", null=True,
                                            verbose_name=_("Short English Description"),
                                            help_text=_("This is english short description"))
    description_en = models.TextField(
        verbose_name=_("English description"), null=True, blank=True, default="",
        help_text=_("This is english description for website")
    )
    description_fa = models.TextField(
        verbose_name=_("Persian description"), null=True, blank=True, default="",
        help_text=_("This is persian description for website")
    )
    address_fa = models.CharField(max_length=400, blank=True, default=_("Please enter your persian site address"),
                                  null=True, verbose_name=_("Persian Address"),
                                  help_text=_("This is persian address for your website"))
    address_en = models.CharField(max_length=400, blank=True, default=_("Please enter your persian site address"),
                                  null=True, verbose_name=_("English Address"),
                                  help_text=_("This is english address for your website"))
    url = models.URLField(max_length=90, verbose_name=_("Website Link"), blank=True, null=True,
                          default=_("Please complete site url"),
                          help_text=_("This is url or link your website without 'http://'"))
    version = models.FloatField(verbose_name=_("Site Version"), default=1.0,
                                help_text=_("This is site version - default = 1.0"))
    phone = models.CharField(validators=[
        validators.RegexValidator(regex='^(\+98|0)?9\d{9}$',
                                  message=_("Phone number must be entered in the true IR (iran) format."),
                                  code=_('invalid IR phone number'))
    ],
        max_length=13, verbose_name=_("Phone"),
        help_text=_("This is IR phone number of sender"))

    email = models.EmailField(max_length=80, null=True, blank=True, verbose_name=_("Email Address"),
                              help_text=_("This is email address for your website"))
    about_fa = models.TextField(verbose_name="Persian About-us", default="Please enter persian about-us text",
                                help_text=_("This is persian about text for your website"), null=True, blank=True)
    about_en = models.TextField(verbose_name="English About-us", default="Please enter english about-us text",
                                help_text=_("This is english about text for your website"), null=True, blank=True)
    small_logo = models.ImageField(
        upload_to=Controllers.Image.img_renamer, verbose_name=_("Small Logo"), null=True, blank=True, default="",
        help_text=_("This is small image logo for website"))
    large_logo = models.ImageField(
        upload_to=Controllers.Image.img_renamer, verbose_name=_("Large Logo"), null=True, blank=True, default="",
        help_text=_("This is large image logo for website"))
    footer_msg_fa = models.CharField(max_length=360, null=True, blank=True, verbose_name=_("Persian Footer Message"),
                                     default=_(
                                         "Please enter your desired message in the admin field - bottom message field"),
                                     help_text=_("This is persian footer message"))
    footer_msg_en = models.CharField(max_length=360, null=True, blank=True, verbose_name=_("English Footer Message"),
                                     default="Please complete footer message in admin - settings",
                                     help_text=_("This is english footer message"))

    class Meta:
        verbose_name = _("Site Setting")
        verbose_name_plural = _("Site Settings")

    @property
    def url_full(self):
        return f"http://{self.url}"

    @property
    def description(self):
        return self.description_en if get_language() == "en-US" else self.description_fa

    @property
    def short_description(self):
        return self.short_description_en if get_language() == "en-US" else self.short_description_fa

    @property
    def title(self):
        return self.title_en if get_language() == "en-US" else self.title_fa

    @property
    def address(self):
        return self.address_en if get_language() == "en-US" else self.address_fa

    @property
    def about(self):
        return self.about_en if get_language() == "en-US" else self.about_fa

    @property
    def sub_title(self):
        return self.sub_title_en if get_language() == "en-US" else self.sub_title_fa

    @property
    def footer_msg(self):
        return self.footer_msg_en if get_language() == "en-US" else self.footer_msg_fa

    @property
    def full_title(self):
        return f"{self.title} {self.sub_title}"

    def __str__(self):
        return self.full_title


class Contact(TimeStampMixin):
    is_read = models.BooleanField(default=False, verbose_name=_("Readed"), help_text=_("This is Readed Message"))
    user = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name=_("User contact"),
                             help_text=_("This user id to send message"))
    name = models.CharField(max_length=50, verbose_name=_("Sender Name"), help_text=_("This is name of sender message"))
    phone = models.CharField(validators=[
        validators.RegexValidator(regex='^(\+98|0)?9\d{9}$',
                                  message=_("Phone number must be entered in the true IR (iran) format."),
                                  code=_('invalid IR phone number'))
    ],
        max_length=13, verbose_name=_("Phone"),
        help_text=_("This is IR phone number of sender"))
    email = models.EmailField(max_length=80, verbose_name=_("Email"), help_text=_("This is mail address of sender"),
                              null=True, blank=True)
    msg = models.TextField(verbose_name=_("Message"), help_text=_("This is message of sender"))

    def read_msg(self):
        self.is_read = True
        self.save()
        return True


class Meta:
    verbose_name = _("Contact Message")
    verbose_name_plural = _("Contact Messages")


def __str__(self):
    return self.name
