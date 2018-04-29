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

def sort(request):
  brand=None
  select_type = request.POST.get("select_type")
  select_criteria = request.POST.get("select_criteria")

  bikes = Bike.objects.all()
  brands = Brand.objects.all()
  if select_type =="all":
    return render(request, 'bikes/bike/list.html', {'brand': brand,'brands': brands,'bikes': bikes})
  elif select_type =="alphabetically":
    if select_criteria=="High to Low":
      bikes= Bike.objects.order_by("title")
      return render(request, 'bikes/bike/list.html', {'brand': brand,'brands': brands,'bikes': bikes})
    else:
      bikes= Bike.objects.order_by("-title")
      return render(request, 'bikes/bike/list.html', {'brand': brand,'brands': brands,'bikes': bikes})

  elif select_type == "price" :
    if select_criteria=="Low to High":
      bikes= Bike.objects.order_by("price")
      return render(request, 'bikes/bike/list.html', {'brand': brand,'brands': brands,'bikes': bikes})
    else:
      bikes= Bike.objects.order_by("-price")
      return render(request, 'bikes/bikes/list.html', {'brand': brand,'brands': brands,'bikes': bikes})

  elif select_type == "brand" :
    if select_criteria=="Low to High":
      bikes= Bike.objects.order_by("brand")
      return render(request, 'bikes/bike/list.html', {'brand': brand,'brands': brands,'bikes': bikes})
    else:
      bikes= Bike.objects.order_by("-brand")
      return render(request, 'bikes/bikes/list.html', {'brand': brand,'brands': brands,'bikes': bikes})





