from django.shortcuts import render
from category.models import Category
from settings.models import SochialAccount
from products.models import Product


def partial_footer(request, *args, **kwargs):
    context = {
        "sochials": SochialAccount.objects.all(),
        # "footer_msg": Site.objects.all()
        "footer_msg": "تیم دولوپر کمکی مشتاق نظرات و پیشنهادات شماست :)"
    }
    return render(request, "landing/partial/footer.html", context)


def partial_offer(request, *args, **kwargs):
    context = {
        "offers": Product.objects.all().filter(is_offer=True)
    }
    return render(request, "landing/partial/offer.html", context)


def partial_category(request, *args, **kwargs):
    context = {
        "categories": Category.objects.all()[:12]
    }
    return render(request, "landing/partial/category.html", context)


def partial_search(request, *args, **kwargs):
    context = {
        "categories": Category.objects.all()[:12]
    }
    return render(request, "landing/partial/search.html", context)