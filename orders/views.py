from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from cart.cart import Cart
from .models import Order, OrderItem
from .forms import CheckoutForm


@login_required
def checkout(request):
    cart = Cart(request)

    if len(cart) == 0:
        messages.warning(request, 'Your cart is empty!')
        return redirect('store:product_list')

    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            # Create order
            order = form.save(commit=False)
            order.user = request.user
            order.total_price = cart.get_total_price()
            order.save()

            # Create order items & update stock
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    price=item['price'],
                    quantity=item['quantity'],
                )
                # Reduce stock
                product = item['product']
                product.stock -= item['quantity']
                product.save()

            # Clear cart
            cart.clear()

            messages.success(
                request,
                f'Order #{order.id} placed successfully! Thank you!'
            )
            return redirect('orders:order_confirm', order_id=order.id)
        else:
            messages.error(request, 'Please fix the errors below.')
    else:
        # Pre-fill form if user is logged in
        initial = {}
        if request.user.is_authenticated:
            initial = {
                'first_name': request.user.first_name,
                'last_name': request.user.last_name,
                'email': request.user.email,
            }
        form = CheckoutForm(initial=initial)

    context = {
        'cart': cart,
        'form': form,
    }
    return render(request, 'orders/checkout.html', context)


@login_required
def order_confirm(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, 'orders/order_confirm.html', {'order': order})


@login_required
def order_list(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'orders/order_list.html', {'orders': orders})


@login_required
def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, 'orders/order_detail.html', {'order': order})