from django.db import models
from bikes.models import Bike



class Bike(models.Model):
    name = models.CharField(max_length=200)
    
    
        
    def __unicode__(self):
        return self.name


    bike = models.ForeignKey(Bike)
    pub_date = models.DateTimeField('date published')
    user_name = models.CharField(max_length=100)
    comment = models.CharField(max_length=200)
