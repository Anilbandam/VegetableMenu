
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import transaction
from decimal import Decimal

from .models import order, orderitems
from cart.models import cart, cartitems


# 1. CHECKOUT VIEW
@login_required
def checkout(request):

    cart_obj = get_object_or_404(
        cart,
        user=request.user
    )

    items = cartitems.objects.filter(
        cart=cart_obj
    ).select_related('product')

    total = Decimal('0.00')

    for item in items:
        total += Decimal(str(item.product.price)) * item.quantity

    return render(request, 'orders/checkout.html', {
        'items': items,
        'total': total
    })


# 2. CONFIRM ORDER VIEW
@login_required
def confirm_order(request):

    if request.method != 'POST':
        return redirect('checkouturls')

    with transaction.atomic():

        cart_obj = get_object_or_404(
            cart.objects.select_for_update(),
            user=request.user
        )

        items = list(
            cartitems.objects.filter(
                cart=cart_obj
            ).select_related('product')
        )

        if not items:
            messages.error(request, "Your cart is empty!")
            return redirect('displaycarturls')

        total = Decimal('0.00')

        # Calculate grand total
        for item in items:
            total += (
                Decimal(str(item.product.price))
                * item.quantity
            )

        # Create main order
        order_obj = order.objects.create(
            user=request.user,
            total_amount=total,
            status='Confirmed'
        )

        # Create individual order items
        for item in items:

            orderitems.objects.create(
                order=order_obj,
                product=item.product,
                product_name=item.product.prdname,
                price=item.product.price,
                quantity=item.quantity
            )

        # Clear cart after successful order creation
        cartitems.objects.filter(
            cart=cart_obj
        ).delete()

    messages.success(
        request,
        "Your order has been placed successfully!"
    )

    return redirect(
        'order_success',
        order_id=order_obj.orderid
    )


# 3. ORDER SUCCESS VIEW
@login_required
def order_success(request, order_id):

    order_obj = get_object_or_404(
        order,
        orderid=order_id,
        user=request.user
    )

    items = orderitems.objects.filter(
        order=order_obj
    ).select_related('product')

    return render(
        request,
        'orders/order_success.html',
        {
            'order': order_obj,
            'items': items
        }
    )


# 4. MY ORDERS VIEW
@login_required
def my_orders(request):

    orders = order.objects.filter(
        user=request.user
    ).prefetch_related(
        'order_items'
    ).order_by('-create_at')

    return render(
        request,
        'orders/orders.html',
        {
            'orders': orders
        }
    )
