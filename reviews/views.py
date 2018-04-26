from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import Review
from bikes.models import Bike
from .forms import ReviewCreateForm
import datetime


def review_list(request):
    latest_review_list = Review.objects.order_by('-pub_date')[:9]
    context = {'latest_review_list':latest_review_list}
    return render(request, 'reviews/review_list.html', context)


def review_detail(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    return render(request, 'reviews/review_detail.html', {'review': review})



def add_review(request):
    cart = Cart(request)
    #bike = get_object_or_404(Bike, id=bike_id)
    user_id = request.user.id
    current_user_object = User.objects.get(id=user_id)
    form = ReviewCreateForm(request.POST)
    if form.is_valid():
        comment = form.cleaned_data['comment']
        user_name = form.cleaned_data['user_name']
        review = Review()
        review.bike = bike
        review.user_name = user_name
        review.comment = comment
        review.pub_date = datetime.datetime.now()
        review.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('reviews:bike_detail', args=(bike.id,)))

    return render(request, 'reviews/bike_detail.html', {'bike': bike, 'form': form})

