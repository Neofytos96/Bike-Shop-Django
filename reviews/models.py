from django.db import models
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from bikes.models import Bike


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    pub_date = models.DateTimeField(auto_now_add=True)
    bike = models.ForeignKey(Bike, on_delete=models.CASCADE, related_name='bike')
    review = models.CharField(max_length = 500, db_index=True)

    class Meta:
        reviewing = ('-created',)

    def __str__(self):
        return 'Review {}'.format(self.id)

    def get_review(self):
        return self.review


class ReviewItem(models.Model):
    review = models.ForeignKey(Review, related_name='items')
    bike = models.ForeignKey(Bike, related_name='review_items')
    pub_date = models.DateTimeField(auto_now_add=True)
    review = models.CharField(max_length = 500, db_index=True)



    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.review
