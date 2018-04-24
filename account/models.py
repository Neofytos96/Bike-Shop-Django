from __future__ import unicode_literals

from django.db import models

class user(models.Model):
    username = models.CharField(blank = True, null = True)
    first_name = models.CharField(blank = True, null = True)
    last_name = models.CharField(blank = True, null = True)
    street = models.CharField(blank = True, null = True)
    city = models.CharField(blank = True, null = True)
    postcode = models.CharField(blank = True, null = True)
    slug = models.SlugField(max_length=30, db_index = True)

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)

   