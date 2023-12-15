from django.shortcuts import render
from store.models import Product, ReviewRating
from django.db.models import Avg
'''
def home(request):
    products = Product.objects.all().filter(is_available=True).order_by('created_date')

    # Get the reviews
    reviews = None
    for product in products:
        reviews = ReviewRating.objects.filter(product_id=product.id, status=True)

    context = {
        'products': products,
        'reviews': reviews,
    }
    return render(request, 'home.html', context)
'''

def home(request):
    # Menggunakan annotate untuk menambahkan kolom rating_avg pada setiap produk
    products = Product.objects.filter(is_available=True).annotate(rating_avg=Avg('reviewrating__rating')).order_by('-rating_avg', 'created_date')

    context = {
        'products': products,
    }
    return render(request, 'home.html', context)