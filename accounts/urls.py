from django.urls import path
from . import views
urlpatterns = [
    path('register/',views.register,name='registerurls'),
    path('login/',views.login1,name='loginurls'),
    path('logout',views.logout1,name='logouturls'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]
