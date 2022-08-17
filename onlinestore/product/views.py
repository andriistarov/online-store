from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def product(request, product_name):
    context = {
        'product_name': product_name,
        'title': "Apple iPhone 13",
        'models': 'Pro Max',
        'color': 'Graphite',
        'screen': '6,7"',
        'memory': '256 GB',
        'camera': '12 MP',
        'dimensions': '78.1x160.8x7.65 mm',
        'price': '48 999 UAH',
    }
    return render(request, 'product_page.html', context)


