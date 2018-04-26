from django.db import models
from bikes.models import Bike


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
    user_name = models.CharField(max_length=100)
    comment = models.CharField(max_length=200)
    rating = models.IntegerField(choices=RATING_CHOICES)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return 'Review {}'.format(self.id)

class ReviewItem(models.Model):
    review = models.ForeignKey(Review, related_name='items')
    bike = models.ForeignKey(Bike, related_name='review_items')
    comment = models.CharField(max_length=200)
    user_name = models.CharField(max_length=100)

    def __str__(self):
        return '{}'.format(self.id)

