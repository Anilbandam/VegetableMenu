
from django.db import models
from django.contrib.auth.models import User
from products.models import products


class order(models.Model):

    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Confirmed', 'Confirmed'),
        ('Shipped', 'Shipped'),
        ('Delivered', 'Delivered'),
        ('Cancelled', 'Cancelled'),
    ]

    orderid = models.AutoField(primary_key=True)

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='orders'
    )

    create_at = models.DateTimeField(auto_now_add=True)

    total_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Pending'
    )

    def __str__(self):
        return f"Order {self.orderid}"


class orderitems(models.Model):

    orderitemid = models.AutoField(primary_key=True)

    order = models.ForeignKey(
        order,
        on_delete=models.CASCADE,
        related_name='order_items'
    )

    product = models.ForeignKey(
        products,
        on_delete=models.SET_NULL,
        null=True
    )

    product_name = models.CharField(max_length=150)

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    quantity = models.PositiveIntegerField()

    @property
    def subtotal(self):
        return self.price * self.quantity

    def __str__(self):
        return self.product_name
