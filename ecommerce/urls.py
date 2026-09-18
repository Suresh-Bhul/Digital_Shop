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

urlpatterns = [
    path('admin/', admin.site.urls),

    # Rest APIs
    path('api/', include('products.api.urls')),
    path('api/', include('cart.api.urls')),


    # Server-rendered frontend
    path('', product_views.index, name='index'),
    path('cart/', cart_views.cart_page, name='cart-page'),


]
