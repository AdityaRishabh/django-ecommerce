from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='home'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),

    path('dashboard/', views.dashboard_view, name='dashboard'),

    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart_view, name='cart'),

    path('increase/<int:item_id>/', views.increase_quantity, name='increase'),
    path('decrease/<int:item_id>/', views.decrease_quantity, name='decrease'),
    path('remove/<int:item_id>/', views.remove_item, name='remove'),

    path('checkout/', views.checkout, name='checkout'),

    path('orders/', views.orders_view, name='orders'),
    path('order/<int:order_id>/', views.order_detail, name='order_detail'),
]