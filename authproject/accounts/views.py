from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Product, Cart, CartItem, Order, OrderItem

# Django RestFramework IMPORTS
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .serializers import ProductSerializer, CartItemSerializer, OrderSerializer

#  AUTHENTICATION

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user_obj = User.objects.get(email=email)
            username = user_obj.username
        except User.DoesNotExist:
            username = None
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid email or password")

    return render(request, 'login.html')


def signup_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists")
            return redirect('signup')

        user = User.objects.create_user(
            username=email,
            email=email,
            password=password
        )

        user.save()
        messages.success(request, "Account created successfully")
        return redirect('login')

    return render(request, 'signup.html')

def logout_view(request):
    logout(request)
    return redirect('login')

# 🏠 DASHBOARD

@login_required
def dashboard_view(request):
    query = request.GET.get('q')
    if query:
        products = Product.objects.filter(name__icontains=query)
    else:
        products = Product.objects.all()
    return render(request, 'dashboard.html', {
        'products': products,
        'query': query
    })

#  CART


@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    cart, _ = Cart.objects.get_or_create(user=request.user)
    item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        item.quantity += 1
        item.save()
    return redirect('cart')

@login_required
def cart_view(request):
    cart, _ = Cart.objects.get_or_create(user=request.user)
    items = CartItem.objects.filter(cart=cart)
    for item in items:
        item.subtotal = item.product.price * item.quantity
    total = sum(item.subtotal for item in items)
    return render(request, 'cart.html', {
        'items': items,
        'total': total
    })


@login_required
def increase_quantity(request, item_id):
    item = get_object_or_404(CartItem, id=item_id)
    item.quantity += 1
    item.save()
    return redirect('cart')


@login_required
def decrease_quantity(request, item_id):
    item = get_object_or_404(CartItem, id=item_id)

    if item.quantity > 1:
        item.quantity -= 1
        item.save()
    else:
        item.delete()

    return redirect('cart')


@login_required
def remove_item(request, item_id):
    item = get_object_or_404(CartItem, id=item_id)
    item.delete()
    return redirect('cart')

# 💳 CHECKOUT


@login_required
def checkout(request):
    cart = Cart.objects.get(user=request.user)
    items = CartItem.objects.filter(cart=cart)
    if not items:
        return redirect('cart')
    total = sum(item.product.price * item.quantity for item in items)
    if request.method == 'POST':
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        order = Order.objects.create(
            user=request.user,
            total_amount=total,
            address=address,
            phone=phone
        )
        for item in items:
            OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity
            )
        items.delete()
        messages.success(request, "Order placed successfully (COD)!")
        return redirect('orders')
    return render(request, 'checkout.html', {
        'items': items,
        'total': total
    })



#  ORDERS

@login_required
def orders_view(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'orders.html', {'orders': orders})


@login_required
def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    items = OrderItem.objects.filter(order=order)

    return render(request, 'order_detail.html', {
        'order': order,
        'items': items
    })

#  REST APIs

#  Product API (Public)
@api_view(['GET'])
def api_products(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


#  Cart API (User specific)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def api_cart(request):
    cart, _ = Cart.objects.get_or_create(user=request.user)
    items = CartItem.objects.filter(cart=cart)
    serializer = CartItemSerializer(items, many=True)
    return Response(serializer.data)


# Order API (User specific)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def api_orders(request):
    orders = Order.objects.filter(user=request.user)
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)