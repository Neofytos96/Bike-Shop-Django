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
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    comment = models.CharField(max_length=200)
    rating = models.IntegerField(choices=RATING_CHOICES)

    class Meta:
        ordering = ('-pub_date',)

    def __str__(self):
        return 'Review {}'.format(self.id)

    def get_review(self):
        return 'Review {}'.format(self.id)
