from django.shortcuts import render, get_object_or_404
from .models import Product

# Create your views here.
def product_list(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'shop/products_list.html', context)

def product_detail(request, product_id):
    """ A view to show individual product details """
    
    product = get_object_or_404(Product, id=product_id)

    context = {
        'product': product,
    }

    return render(request, 'shop/product_detail.html', context)