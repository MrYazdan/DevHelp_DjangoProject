from django.shortcuts import render
from category.models import Category
from settings.models import SochialAccount, Site
from products.models import Product


def partial_footer(request, *args, **kwargs):
    context = {
        "sochials": SochialAccount.objects.all(),
        "footer_msg": Site.objects.last().footer_msg
    }
    return render(request, "landing/partial/footer.html", context)


def partial_offer(request, *args, **kwargs):
    context = {
        "offers": Product.objects.all().filter(is_offer=True)
    }
    return render(request, "landing/partial/offer.html", context)


def partial_category(request, *args, **kwargs):
    context = {
        "categories": Category.objects.all()[:12] if len(Category.objects.all()) >= 12 else Category.objects.all()[:6]
    }
    return render(request, "landing/partial/category.html", context)


def partial_search(request, *args, **kwargs):
    context = {}
    return render(request, "landing/partial/search.html", context)


def partial_header(request, *args, **kwargs):
    context = {
        "site": Site.objects.last()
    }
    return render(request, "landing/partial/header.html", context)


def partial_nav(request, *args, **kwargs):
    context = {
        "user": request.user if request.user.username else None
    }
    return render(request, "landing/partial/nav.html", context)
