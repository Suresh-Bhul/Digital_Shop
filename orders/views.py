from django.shortcuts import render


def checkout_page(request):
    """
    Authentication is enforced by the
    JavaScript layer (checkout.js) which redirects to /login/ if no
    valid JWT access token is present, and by the API itself.
    """
    return render(request, 'checkout.html')


def orders_page(request):
    return render(request, 'orders.html')


def order_detail_page(request, pk):
    return render(request, 'order-detail.html', {'order_id': pk})
