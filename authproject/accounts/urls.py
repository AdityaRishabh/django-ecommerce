from django.urls import path
from . import views

# JWT IMPORTS
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [

    #  AUTH 

    path('', views.login_view, name='home'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),


    #  DASHBOARD (UI)

    path('dashboard/', views.dashboard_view, name='dashboard'),


    #  CART (UI)

    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart_view, name='cart'),
    path('increase/<int:item_id>/', views.increase_quantity, name='increase'),
    path('decrease/<int:item_id>/', views.decrease_quantity, name='decrease'),
    path('remove/<int:item_id>/', views.remove_item, name='remove'),

    # CHECKOUT (UI)

    path('checkout/', views.checkout, name='checkout'),

    #  ORDERS (UI)

    path('orders/', views.orders_view, name='orders'),
    path('order/<int:order_id>/', views.order_detail, name='order_detail'),

    #  PRODUCT APIs

    path('api/products/', views.api_products, name='api_products'),
    path('api/add-product/', views.api_add_product, name='api_add_product'),
    path('api/update-product/<int:pk>/', views.api_update_product, name='api_update_product'),
    path('api/delete-product/<int:pk>/', views.api_delete_product, name='api_delete_product'),

    #  CART APIs
    
    path('api/cart/', views.api_cart, name='api_cart'),
    path('api/add-to-cart/', views.api_add_to_cart, name='api_add_to_cart'),
    path('api/update-cart/<int:item_id>/', views.api_update_cart, name='api_update_cart'),
    path('api/remove-cart/<int:item_id>/', views.api_remove_cart, name='api_remove_cart'),

    
    # ORDER APIs
    
    path('api/orders/', views.api_orders, name='api_orders'),
]