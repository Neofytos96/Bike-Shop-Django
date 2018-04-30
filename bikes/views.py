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


"""def post_list(request):
    template = 'bikes/bike/list.html'
    object_list = Post.objects.filter(status='Published')

    pages = pagination(request, object_list, num=1)

    context = {
        'items': pages[0],
        'page_range': pages[1],
    }
    return render(request, template, context)


def post_detail(request, slug):
    template = 'blog/post_detail.html'

    post = get_object_or_404(Post, slug=slug)
    context = {
        'post': post,
    }
    return render(request, template, context)


def category_detail(request, slug):
    template = 'blog/category_detail.html'

    category = get_object_or_404(Category, slug=slug)
    post = Post.objects.filter(category=category)

    context = {
        'category': category,
        'post': post,
    }
    return render(request, template, context)"""

def search(request):
    template = 'bikes/bike/list.html'


    query = request.GET.get('q')

    if query:
        queryset_list = Bike.objects.filter(Q(title__icontains=query)).distinct()
    #else:
    #    results = Bike.objects.filter(status="Published")

    paginator = Paginator(queryset_list,10)
    page_request_var = "page"
    page = request.GET.get(page_request_var)
    try: 
      queryset = paginator.page(page)
    except:
      queryset = paginator.page(1)
    except EmptyPage:
      queryset = paginator.page(paginator.num_pages)


    context = {
        "object_list": queryset,
        "title": "List",
        "page_request_var": page_request_var,
    }
    return render(request, template, context)




