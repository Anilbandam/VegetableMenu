from decimal import Decimal
from django.shortcuts import render, redirect, get_object_or_404
from .models import cart, cartitems
from django.contrib.auth.decorators import login_required
from products.models import products
@login_required(login_url='loginurls')
def addcart(request, pk):

    if request.method == "POST":

        # Get or create cart for logged-in user
        cartobj, created = cart.objects.get_or_create(
            user=request.user
        )

        # Get selected product
        prdobj = get_object_or_404(products, prdno=pk)

        # Check whether product already exists in cart
        item, created = cartitems.objects.get_or_create(
            cart=cartobj,
            product=prdobj,
            defaults={'quantity': 1}
        )

        # If product already exists, increase quantity
        if not created:
            item.quantity += 1
            item.save()

        return redirect('displaycarturls')


@login_required(login_url='loginurls')
def displaycart(request):
    cartobj = cart.objects.filter(user=request.user).first()

    total = Decimal('0.00')
    total_quantity = 0

    if cartobj:
        items1 = cartitems.objects.filter(
            cart=cartobj
        ).select_related('product')

        for item in items1:
            item.subtotal = item.product.price * item.quantity
            total += item.subtotal
            total_quantity += item.quantity
    else:
        items1 = cartitems.objects.none()

    return render(request, 'cart/cart.html', {
        'items': items1,
        'total': total,
        'total_quantity': total_quantity
    })


@login_required(login_url='loginurls')
def increase_quantity(request, pk):

    item = get_object_or_404(
        cartitems,
        pk=pk,
        cart__user=request.user
    )

    item.quantity += 1
    item.save()

    return redirect('displaycarturls')

@login_required(login_url='loginurls')
def decrease_quantity(request, pk):
    if request.method == "POST":
        item = cartitems.objects.filter(
            pk=pk,
            cart__user=request.user
        ).first()

        # If item does not exist, go back to cart
        if item is None:
            return redirect('displaycarturls')

        if item.quantity > 1:
            item.quantity -= 1
            item.save()
        else:
            item.delete()

    return redirect('displaycarturls')
