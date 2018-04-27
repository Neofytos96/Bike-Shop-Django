from django.db import models
from bikes.models import Bike
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate



class Review(models.Model):
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    bike = models.ForeignKey(Bike)
    pub_date = models.DateTimeField('date published')
    user_name = models.CharField(max_length=40)
    comment = models.CharField(max_length=200)
    rating = models.IntegerField(choices=RATING_CHOICES)

    class Meta:
        ordering = ('-pub_date',)

    def __str__(self):
        return 'Review {}'.format(self.id)

    def get_review(self):
        return 'Review {}'.format(self.id)


class ReviewItem(models.Model):
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    review = models.ForeignKey(Review, related_name='items')
    bike = models.ForeignKey(Bike, related_name='review_items')
    user_name = models.CharField(max_length=40)
    comment = models.CharField(max_length=200)
    rating = models.IntegerField(choices=RATING_CHOICES)
    pub_date = models.DateTimeField('date published')


    def __str__(self):
        return '{}'.format(self.id)

    def get_the_review(self):
        return '{}'.format(self.id)