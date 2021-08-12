from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from order.models import OrderItem, Order, Status
from products.models import Product, OffCode


def cart(request):
    if request.user.is_authenticated:
        order = Order.objects.filter(owner=request.user, payment_datetime=None).first()
        offcode = order.offcode if order.offcode else None
        context = {
            "empty": False,
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
    order = Order.objects.filter(payment_datetime=None).first()
    if request.method == "GET":
        if order is None:
            status = Status.objects.get(id=1)
            order = Order.objects.create(owner=request.user, status=status)
        # filter products by id
        product = Product.objects.filter(id=request.GET.get('item_id')).first()
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

    # offcode input
    elif request.method == 'POST':
        code = request.POST["code"]
        offcode = OffCode.objects.get(code=code)
        # check permission
        check = offcode.checker(request.user)
        # off code activity
        if check:
            order.offcode = offcode
            order.save()
        return redirect(reverse('cart'))


# @login_required(login_url="/account/login")
# def modify_offer(request, **kwargs):
#     code = kwargs.get("code")
#     offcode = OffCode.objects.get(code=code)
#     check = offcode.checker(request.user)
#     order = Order.objects.filter(owner=request.user, payment_datetime=None).first()
#
#     if order and check:
#         order.offcode = offcode
#         order.save()
#         status = "OK"
#         return JsonResponse({
#             "status": status
#         })
