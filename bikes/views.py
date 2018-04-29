from django.shortcuts import render, get_object_or_404
from django.db.models import Q
#from example.config import pagination
from django.core.paginator import Paginator
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
    if select_criteria=="Descending":
      bikes= Bike.objects.order_by("title")
      return render(request, 'bikes/bike/list.html', {'brand': brand,'brands': brands,'bikes': bikes})
    else:
      bikes= Bike.objects.order_by("-title")
      return render(request, 'bikes/bike/list.html', {'brand': brand,'brands': brands,'bikes': bikes})

  elif select_type == "price" :
    if select_criteria=="Ascending":
      bikes= Bike.objects.order_by("price")
      return render(request, 'bikes/bike/list.html', {'brand': brand,'brands': brands,'bikes': bikes})
    else:
      bikes= Bike.objects.order_by("-price")
      return render(request, 'bikes/bike/list.html', {'brand': brand,'brands': brands,'bikes': bikes})

  elif select_type == "release_date" :
    if select_criteria=="Ascending":
      bikes= Bike.objects.order_by("release_date")
      return render(request, 'bikes/bike/list.html', {'brand': brand,'brands': brands,'bikes': bikes})
    else:
      bikes= Bike.objects.order_by("-release_date")
      return render(request, 'bikes/bike/list.html', {'brand': brand,'brands': brands,'bikes': bikes})


def search(request):
  template = 'bikes/bike/list.html'
  query = request.GET.get('q')
  results = Bike.objects.filter(Q(title__icontains=q) | Q(brand__icontains=q))
  pages = pagination(request, results, num=1)
  context = {'items':pages[0], 'page_range':pages[1],}
  return render(request, template, context)


import operator

from django.db.models import Q


class BlogSearchListView(BlogListView):
    """
    Display a Blog List page filtered by the search query.
    """
    paginate_by = 10

    def get_queryset(self):
        result = super(BlogSearchListView, self).get_queryset()

        query = self.request.GET.get('q')
        if query:
            query_list = query.split()
            result = result.filter(
                reduce(operator.and_,
                       (Q(title__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                       (Q(content__icontains=q) for q in query_list))
            )

        return result
  


