from decimal import Decimal
from django.conf import settings
from bikes.models import Bike

class Account(object):
 
    def get_user_label(self, user):
        name = user.get_full_name()
        username = user.username

        return name
        
            
   