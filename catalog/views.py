from django.http import HttpResponse
from django.shortcuts import render

from catalog.models import Product


def home(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'home.html', context)


def contacts(request):
    if request.method == 'POST':
        return HttpResponse("Сообщение отправлено")
    else:
        return render(request, 'contacts.html')


def product_info(request, pk):
    product = Product.objects.get(id=pk)
    context = {'product': product}
    return render(request, 'product_info.html', context)
