from django.shortcuts import render
from settings.models import SochialAccount
from products.models import Product


def partial_footer(request, *args, **kwargs):
    context = {
        "sochials": SochialAccount.objects.all(),
        # "footer_msg": SiteSettings.objects.all()
        "footer_msg": "تیم دولوپر کمکی مشتاق نظرات و پیشنهادات شماست :)"
    }
    return render(request, "landing/partial/footer.html", context)


def partial_offer(request, *args, **kwargs):
    context = {
        "offers": Product.objects.all().filter(is_offer=True)
    }
    return render(request, "landing/partial/offer.html", context)
