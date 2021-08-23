from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from core.models import Address
from order.models import Order, Status
from products.models import Product, OffCode
from jdatetime import datetime as dt


def cart(request):
    if request.user.is_authenticated:
        order = Order.objects.get(owner=request.user, payment_datetime=None) if \
            Order.objects.filter(owner=request.user, payment_datetime=None) else \
            Order.objects.create(owner=request.user, status=Status.objects.get(id=1))
        offcode = order.offcode if order.offcode else None
        context = {
            "empty": False if order.orderitem_set.all() else True,
            "user": request.user,
            "order": order,
            "offcode": offcode,
            "items": order.orderitem_set.all(),
        }
        return render(request, "landing/cart.html", context)
    else:
        context = {
            "empty": True,
            "user": request.user if request.user.username else None,
        }
        return render(request, "landing/cart.html", context)


@login_required(login_url="/account/login")
def add_to_cart(request, **kwargs):
    order = Order.objects.get(owner=request.user, payment_datetime=None) if \
            Order.objects.filter(owner=request.user, payment_datetime=None) else \
            Order.objects.create(owner=request.user, status=Status.objects.get(id=1))
    if request.method == "GET":
        if order is None:
            status = Status.objects.get(id=1)
            order = Order.objects.create(owner=request.user, status=status)
        # get products by id
        product = Product.objects.get(id=request.GET.get('item_id'))
        # check for orderitem in cart
        orderitem = order.orderitem_set.filter(product=product).first()
        if orderitem:
            orderitem.count += 1
            orderitem.save()
        else:
            # create orderItem of the selected product
            order.orderitem_set.create(order=order, product=product, price=product.price, count=1)
        # show cart page
        return redirect(reverse('cart'))


@login_required(login_url="/account/login")
def recepie(request, **kwargs):
    if request.method == "GET":
        order = get_object_or_404(Order, recepie_id=kwargs["recepie_id"])
        context = {
            "order": order,
            "items": order.orderitem_set.all(),
        }
        return render(request, "landing/recepie.html", context)


@login_required(login_url="/account/login")
def final(request, **kwargs):
    order = Order.objects.get(owner=request.user, payment_datetime=None) if \
        Order.objects.filter(owner=request.user, payment_datetime=None) else \
        Order.objects.create(owner=request.user, status=Status.objects.get(id=1))
    if request.method == "GET":
        if not order.orderitem_set.all():
            # redirect user if your cart is empty !
            return redirect(reverse('cart'))

        context = {
            "order": order,
            "addresses": Address.objects.filter(owner=request.user)
        }
        return render(request, "landing/final.html", context)

    elif request.method == "POST":
        if order.orderitem_set.all():
            # get address
            address_id = int(request.POST['address_id'])
            address = Address.objects.get(id=address_id)
            order.address = address
            order.save()
            # check off code used
            if order.offcode:
                offcode = order.offcode
                if offcode.expire_checker():
                    offcode.last_used = dt.now()
                    offcode.count_use -= 1
                    offcode.save()
            # change status and payment_time :
            order.paid()
            # update product detail
            for i in order.orderitem_set.all():
                product = i.product
                product.sell(i.count)
                product.save()
            # redirect in recepie page :
            return redirect(reverse('recepie'), recepie_id=order.recepie_id)
        else:
            return redirect(reverse('cart'))
