from django.urls import path
from . import views

urlpatterns = [
    path('cartpage/<int:pk>/', views.addcart, name='carturls'),
    path('cartpage/', views.displaycart, name='displaycarturls'),
    path('increase/<int:pk>/', views.increase_quantity, name='increaseurls'),
    path('decrease/<int:pk>/', views.decrease_quantity, name='decreaseurls'),
]