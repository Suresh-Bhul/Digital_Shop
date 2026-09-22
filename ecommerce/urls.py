"""
URL configuration for ecommerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

from products import views as product_views
from cart import views as cart_views
from orders import views as order_views
from accounts import views as account_views


urlpatterns = [
    path('admin/', admin.site.urls),

    # Rest APIs
    path('api/', include('accounts.api.urls')),
    path('api/', include('products.api.urls')),
    path('api/', include('cart.api.urls')),
    path('api/', include('orders.api.urls')),
    path('api/', include('payments.api.urls')),


    # Server-rendered frontend
    path('', product_views.index, name='index'),
    path('login/', account_views.login_page, name='login-page'),
    path('register/', account_views.register_page, name='register-page'),
    path('cart/', cart_views.cart_page, name='cart-page'),
    path('product/<int:pk>/', product_views.product_detail, name='product-detail-page'),
    path('checkout/', order_views.checkout_page, name='checkout-page'),
    path('orders/', order_views.orders_page, name='orders-page'),
    path('orders/<int:pk>/', order_views.order_detail_page, name='order-detail-page'),
    


]
