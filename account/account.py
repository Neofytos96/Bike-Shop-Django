from decimal import Decimal
from django.conf import settings
from books.models import Book

class Account(object):
    def __init__(self, request):
        """
        Initialize the cart.
        """
    def get_full_name(self):
        return render(user.get_full_name)