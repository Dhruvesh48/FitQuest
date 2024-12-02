from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category

# Create your views here.
def product_list(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    query = None
    categories = None
    sort_by = request.GET.get('sort')

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)
        if sort_by:
            if sort_by == 'price_asc':
                products = products.order_by('price')
            elif sort_by == 'price_desc':
                products = products.order_by('-price')
            elif sort_by == 'rating_asc':
                products = products.order_by('rating')
            elif sort_by == 'rating_desc':
                products = products.order_by('-rating')
            elif sort_by == 'name_asc':
                products = products.order_by('name')
            elif sort_by == 'name_desc':
                products = products.order_by('-name')
            elif sort_by == 'category_asc':
                products = products.order_by('category__name')  
            elif sort_by == 'category_desc':
                products = products.order_by('-category__name')

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': sort_by,
    }

    return render(request, 'shop/products_list.html', context)

def product_detail(request, product_id):
    """ A view to show individual product details """
    
    product = get_object_or_404(Product, id=product_id)

    context = {
        'product': product,
    }

    return render(request, 'shop/product_detail.html', context)