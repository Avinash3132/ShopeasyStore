from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.views.decorators.http import require_POST
from store.models import Product
from .cart import Cart


def cart_detail(request):
    cart = Cart(request)
    context = {'cart': cart}
    return render(request, 'cart/cart.html', context)


@require_POST
def add_to_cart(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    quantity = int(request.POST.get('quantity', 1))
    cart.add(product=product, quantity=quantity)
    messages.success(request, f'"{product.name}" added to cart!')
    return redirect('cart:cart_detail')


@require_POST
def update_cart(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    quantity = int(request.POST.get('quantity', 1))
    if quantity > 0:
        cart.add(product=product, quantity=quantity, override_quantity=True)
        messages.success(request, 'Cart updated!')
    else:
        cart.remove(product)
        messages.success(request, f'"{product.name}" removed from cart!')
    return redirect('cart:cart_detail')


def remove_from_cart(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    messages.success(request, f'"{product.name}" removed from cart!')
    return redirect('cart:cart_detail')