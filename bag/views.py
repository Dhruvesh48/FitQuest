from django.shortcuts import render, redirect, reverse, HttpResponse

# Create your views here.

def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')

def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

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
            else:
                bag[item_id]['items_by_size'][size] = quantity
        else:
            bag[item_id] = {'items_by_size': {size: quantity}}
    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
        else:
            bag[item_id] = quantity

    request.session['bag'] = bag
    return redirect(redirect_url)

def update_bag_item(request, item_id):
    """Update the quantity of an item in the bag."""
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity'))
        size = request.POST.get('product_size', None)  # For products with sizes
        bag = request.session.get('bag', {})

        if item_id in bag:
            if size:
                if size in bag[item_id]['items_by_size']:
                    if quantity > 0:
                        bag[item_id]['items_by_size'][size] = quantity
                    else:
                        del bag[item_id]['items_by_size'][size]
                        if not bag[item_id]['items_by_size']:
                            bag.pop(item_id)
            else:
                if quantity > 0:
                    bag[item_id]['quantity'] = quantity
                else:
                    bag.pop(item_id)
        
        request.session['bag'] = bag
        return redirect('view_bag')

    return redirect('view_bag')

def remove_from_bag(request, item_id):
    """Remove an item from the bag."""
    try:
        size = request.POST.get('product_size', None)  # For products with sizes
        bag = request.session.get('bag', {})

        if size:
            if size in bag[item_id]['items_by_size']:
                del bag[item_id]['items_by_size'][size]
                if not bag[item_id]['items_by_size']:
                    bag.pop(item_id)
        else:
            bag.pop(item_id)

        request.session['bag'] = bag
        return redirect('view_bag')

    except KeyError:
        return redirect('view_bag')