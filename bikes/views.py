from django.shortcuts import render, get_object_or_404
from .models import Brand, Bike
from cart.forms import CartAddProductForm


def bike_list(request, brand_slug=None):
    brand = None
    brands = Brand.objects.all()
    bikes = Bike.objects.filter(available=True)
    if brand_slug:
        brand = get_object_or_404(Brand, slug=brand_slug)
        bikes = bikes.filter(brand=brand)
       # bikes.order_by(-local_stock)
    return render(request, 'bikes/bike/list.html', {'brand': brand,
                                                      'brands': brands,
                                                      'bikes': bikes})


def bike_detail(request, id, slug):
    bike = get_object_or_404(Bike, id=id, slug=slug, available=True)
    cart_bike_form = CartAddProductForm()
    return render(request,
                  'bikes/bike/detail.html',
                   {'bike': bike,
                    'cart_bike_form': cart_bike_form})
                  #{'book': book})
