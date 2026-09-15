from django.shortcuts import render


def index(request):
    """Homepage - product listing. Data is fetched client-side via the API."""
    return render(request, 'index.html')


def product_detail(request, pk):
    """Product detail page """
    return render(request, 'product-detail.html', {'product_id': pk})
