
from django.urls import path
from . import views

urlpatterns = [
    # Checkout page
    path('checkout/', views.checkout, name='checkouturls'),

    # Confirm order
    path('confirm/', views.confirm_order, name='confirmorderurls'),

    # Order success page
    path(
        'success/<int:order_id>/',
        views.order_success,
        name='order_success'
    ),

    # Customer order history
    path('myorders/', views.my_orders, name='ordersurls'),
]
