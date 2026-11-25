from django.shortcuts import render
from .models import products
from django.contrib.auth.decorators import login_required
@login_required(login_url='loginurls')
def home(request):

    search = request.GET.get('search', '').strip()

    if search:
        obj = products.objects.filter(
            prdname__icontains=search
        )
    else:
        obj = products.objects.all()

    return render(request, 'products/home.html', {
        'product': obj,
        'search': search
    })