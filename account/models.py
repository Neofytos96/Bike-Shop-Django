from __future__ import unicode_literals

from django.db import models

class user(models.Model):
    username = models.CharField(max_length = 30)
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    street = models.CharField(max_length = 30)
    city = models.CharField(max_length = 30)
    postcode = models.CharField(max_length = 30)
    slug = models.SlugField(max_length=30, db_index = True)

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)

   