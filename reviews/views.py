from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import Review
from bikes.models import Bike
from .forms import ReviewCreateForm
import datetime
from cart.cart import Cart




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
    user = request.user.id
    #current_user_object = User.objects.get(id=user_id)
    form = ReviewCreateForm(request.POST)
    if form.is_valid():
        comment = form.cleaned_data['comment']
        #user_name = form.cleaned_data['user_name']
        rating = form.cleaned_data['rating']
        review = Review()
        #review.bike = bike
        #review.user_name = user_name
        #review.comment = comment
#        bike = get_object_or_404(Bike, id=bike_id)
 #       review.pub_date = datetime.datetime.now()
        #review.user = current_user_object
        review.save()
        for item in cart:
            ReviewItem.objects.create(review=review,
                                      bike=item['bike'],
                                      rating=item['rating'],
                                      comment=item['comment'])
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        #return HttpResponseRedirect(reverse('reviews:bike_detail', args=(bike.id,)))
        return render (request, 'reviews/reviews/created.html',{'review':review})
    else:
        return render(request, 'reviews/reviews/create_review.html',{'form': form})