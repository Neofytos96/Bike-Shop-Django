from django.shortcuts import render_to_response, get_object_or_404, render
from django.conf import settings
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Review, ReviewItem
from .forms import ReviewCreateForm
from cart.cart import Cart

def review_create(request):
	cart = Cart(request)
	if request.user.is_authenticated():
		user_id = request.user.id
		current_user_object = User.objects.get(id=user_id)
		form = ReviewCreateForm(request.POST)
			
		if form.is_valid():
			review = form.save(commit=False)
			review.user = current_user_object
			review = form.save()
			#HERE NEED TO CHANGE TO 
			for item in cart:
				ReviewItem.objects.create(review=review,
                                         bike=item['bike'],
                                         pub_date=item['pub_date'],
                                         user=item['user'])
			return render (request, 'review/review/created.html',{'review':review})

		else:
			return render (request, 'order/order/create.html',{'form': form})			
	else:
		return render(request, 'order/order/create-login.html')