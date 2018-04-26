from django.db import models
from bikes.models import Bike
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User


class Review(models.Model):
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    pub_date = models.DateTimeField('date published')
    user_name = models.CharField(max_length=100)
    comment = models.CharField(max_length=200)
    rating = models.IntegerField(choices=RATING_CHOICES)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return 'Review {}'.format(self.id)

    def get_review(self):
        return self.items.all()
