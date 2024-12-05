from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib import messages
from shop.models import Product

# Create your views here.

def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')

def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """
    
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    bag = request.session.get('bag', {})

    if size:
        if item_id in list(bag.keys()):
            if size in bag[item_id]['items_by_size'].keys():
                bag[item_id]['items_by_size'][size] += quantity
                messages.success(request, f'Added size {size.upper()} {product.name} quantity to {bag[item_id]["items_by_size"][size]}')
            else:
                bag[item_id]['items_by_size'][size] = quantity
                messages.success(request, f'Added size {size.upper()} {product.name} to your bag')
                
        else:
            bag[item_id] = {'items_by_size': {size: quantity}}
            messages.success(request, f'Added size {size.upper()} {product.name} to your bag')
    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
            messages.success(request, f'Updated {product.name} quantity to {bag[item_id]}')
        else:
            bag[item_id] = quantity
            messages.success(request, f'Added {product.name} quantity to {bag[item_id]}')

    request.session['bag'] = bag
    return redirect(redirect_url)

def update_bag_item(request, item_id):
    """Update the quantity of an item in the bag."""

    product = get_object_or_404(Product, pk=item_id)
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity'))
        size = None
        if 'product_size' in request.POST:
            size = request.POST['product_size']
        bag = request.session.get('bag', {})

        if size:
            if item_id in list(bag.keys()):
                if size in bag[item_id]['items_by_size'].keys():
                    bag[item_id]['items_by_size'][size] = quantity
                    messages.success(request, f'Updated size {size.upper()} {product.name} quantity to {bag[item_id]["items_by_size"][size]}')
                else:
                    bag[item_id]['items_by_size'][size] = quantity
                    messages.success(request, f'Removed size {size.upper()} {product.name} from your bag')
            else:
                bag[item_id] = {'items_by_size': {size: quantity}}
        else:
            if item_id in list(bag.keys()):
                bag[item_id] = quantity
                messages.success(request, f'Updated {product.name} quantity to {bag[item_id]}')
            else:
                bag[item_id] = quantity
                messages.success(request, f'Removed {product.name} from your bag')
        
        request.session['bag'] = bag
        return redirect('view_bag')

    return redirect('view_bag')

def remove_from_bag(request, item_id):
    """Remove an item from the bag."""

    product = get_object_or_404(Product, pk=item_id)
    try:
        size = request.POST.get('product_size', None)  # For products with sizes
        bag = request.session.get('bag', {})

        if size:
            if size in bag[item_id]['items_by_size']:
                del bag[item_id]['items_by_size'][size]
                if not bag[item_id]['items_by_size']:
                    bag.pop(item_id)
                messages.success(request, f'Removed size {size.upper()} {product.name} from your bag')
        else:
            bag.pop(item_id)
            messages.success(request, f'Removed {product.name} from your bag')

        request.session['bag'] = bag
        return redirect('view_bag')

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)