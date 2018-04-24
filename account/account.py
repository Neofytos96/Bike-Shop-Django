from decimal import Decimal
from django.conf import settings
from books.models import Book

class Account(object):
 
    def get_user_label(self, user):
        name = user.get_full_name()
        username = user.username

        return name
        
            
   