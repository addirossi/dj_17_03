from django.http import HttpResponse, Http404
from django.shortcuts import render

from .models import Product


def sample_controller(request):
    return HttpResponse('Hello world!')


def products_list(request):
    products = Product.objects.all()
    return render(request, 'main/list.html', {'products': products})


def product_details(request, product_id):
    print(f'id товара: {product_id}')
    try:
        product = Product.objects.get(id=product_id)
        return render(request, 'main/details.html', {'prod': product})
    except Product.DoesNotExist:
        raise Http404('Товар не найден')
