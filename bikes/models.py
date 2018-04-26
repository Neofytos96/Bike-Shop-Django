#adapted from https://github.com/guinslym/django-by-example-book
from django.db import models
from django.core.urlresolvers import reverse


class Brand(models.Model):
    brand = models.CharField(max_length = 50)
    slug = models.SlugField(max_length = 50, db_index = True, unique = True)

    class Meta:
        ordering = ('brand',)
        verbose_name = 'brand'
        verbose_name_plural = 'brands'

    def __str__(self):
		return self.brand

    def get_absolute_url(self):
        return reverse('bikes:bike_list_by_brand', args=[self.slug])

class Bike(models.Model):
    brand = models.ForeignKey(Brand, related_name='bikes')
    title = models.CharField(max_length = 100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)
#   image = models.ImageField(upload_to='books/%Y/%m/%d', blank=True)
    image = models.ImageField(upload_to='media/bikes/bikes_img', blank=True)
    description = models.TextField(blank = True, null = True)
    release_date = models.DateField()
    price = models.DecimalField(decimal_places=2, max_digits=10)
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)

    class Meta:
        ordering = ('-price',)
        index_together = (('id', 'slug'),)

    def __str__(self):
    	return self.title

    def get_absolute_url(self):
        return reverse('bikes:bike_detail', args=[self.id, self.slug])

    

