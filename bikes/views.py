from django.shortcuts import render, get_object_or_404
from .models import Category, Bike
from cart.forms import CartAddProductForm


def bike_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    bikes = Bike.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        bikes = bikes.filter(category=category)
    return render(request, 'bikes/bike/list.html', {'category': category,
                                                      'categories': categories,
                                                      'bikes': bikes})


def bike_detail(request, id, slug):
    bike = get_object_or_404(Bike, id=id, slug=slug, available=True)
    cart_bike_form = CartAddProductForm()
    return render(request,
                  'bikes/bike/detail.html',
                   {'bike': bike,
                    'cart_bike_form': cart_bike_form})
                  #{'book': book})
