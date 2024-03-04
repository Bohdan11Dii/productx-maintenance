from django.shortcuts import render, get_object_or_404

from catalog.views import ProductDetailView
from .cart import Cart
from catalog.models import Product
from django.http import JsonResponse
# Create your views here.


def cart_summary(request):
    cart = Cart(request)
    cart_products = cart.get_prods()
    quantities = cart.get_quants
    totals = cart.cart_total()
    
    
    product_id = [product.id for product in cart_products]
    request.session['product_id'] = product_id
    
    context = {
        "cart_products": cart_products,
        "quantities": quantities,
        "totals": totals
    }
    return render(request, "cart/cart_summary.html", context=context)


def cart_add(request):
    cart = Cart(request)
    
    if request.POST.get("action") == "post":
        
        product_id = int(request.POST.get("product_id"))
        product_qty = int(request.POST.get("product_qty"))
        
        
        product = get_object_or_404(Product, id=product_id)
        
        cart.add(product=product, quantity=product_qty)
        
        
        cart_quantity = cart.__len__()
        
        response = JsonResponse({"qty": cart_quantity})
        return response
        
        

def cart_delete(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        # Get stuff
        product_id = int(request.POST.get('product_id'))
        # Call delete Function in Cart
        cart.delete(product=product_id)

        response = JsonResponse({'product':product_id})
        #return redirect('cart_summary')
        return response


def cart_update(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))
        cart.update(product=product_id, quantity=product_qty)
        response = JsonResponse({'qty':product_qty})
        return response
