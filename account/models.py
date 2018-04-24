from __future__ import unicode_literals

from django.db import models

class user(models.Model):
    username = models.TextField(blank = True, null = True)
    first_name = models.TextField(blank = True, null = True)
    last_name = models.TextField(blank = True, null = True)
    street = models.TextField(blank = True, null = True)
    city = models.TextField(blank = True, null = True)
    postcode = models.TextField(blank = True, null = True)

   