from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Order
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

def detail(request, pk):
    single_product = Product.objects.get(id=pk)

    return render(request, 'main/detail.html', {'single_product': single_product})

def checkout(request):
    order = Order()
    if request.method == "POST":
        items = request.POST.get('items', "")
        name = request.POST.get('name', "")
        email = request.POST.get('email', "")
        address = request.POST.get('address', "")
        city = request.POST.get('city', "")
        state = request.POST.get('state', "")
        zipcode = request.POST.get('zipcode', "")
        total = request.POST.get('total', "")
        order = Order(items=items, name=name, email=email, address=address, city=city, state=state, zipcode=zipcode, total=total)
        order.save()


    return render(request, 'main/checkout.html')
