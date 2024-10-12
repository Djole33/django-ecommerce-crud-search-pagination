from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from django.core.paginator import Paginator

# Create your views here.

def index(request):
    product_objects = Product.objects.all()

    item_name = request.GET.get('item_name')
    if item_name is not '' and item_name is not None:
        product_objects = Product.objects.filter(title__icontains=item_name)

    paginator = Paginator(product_objects, 4)
    page = request.GET.get('page')
    product_objects = paginator.get_page(page)

    return render(request, 'main/index.html', {'product_objects': product_objects})
