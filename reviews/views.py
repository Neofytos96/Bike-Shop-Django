from django.shortcuts import render_to_response, get_object_or_404, render
from django.conf import settings
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Review
from bikes.models import Bike
from .forms import ReviewCreateForm
import datetime






#def review_list(request):
#    latest_review_list = Review.objects.order_by('-pub_date')[:9]
#    context = {'latest_review_list':latest_review_list}
#    return render(request, 'reviews/review_list.html', context)


#def review_detail(request, review_id):
#    review = get_object_or_404(Review, pk=review_id)
#    return render(request, 'reviews/review_detail.html', {'review': review})



def review_create(request, bike_id):
    #cart = Cart(request)

    #bike = get_object_or_404(Bike, id=bike_id)
    if request.user.is_authenticated():
        user_id = request.user.id
        current_user_object = User.objects.get(id=user_id)
        form = ReviewCreateForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            #bike = form.save(commit=False)
            review.user = current_user_object
            #bike.user = current_user_object
            user_name = form.cleaned_data['user_name']
            comment = form.cleaned_data['comment']
            rating = form.cleaned_data['rating']
            #bike = form.cleaned_data['bike']
            bike = get_object_or_404(Bike, id=bike_id)
            #bike_id=bike
            pub_date = datetime.datetime.now()
            #review.user = current_user_object
            review = Review()
            review.save()
            ReviewItem.objects.create(review=review,
                                         bike='bike',
                                         comment='comment',
                                         pub_date='quantity',
                                         user_name='user_name',
                                         rating='rating')
            
            return render (request, 'reviews/reviews/created.html',{'review':review})
        else:
            return render(request, 'reviews/reviews/create.html',{'form': form})
    else:
        return render(request, 'reviews/reviews/create-login.html')