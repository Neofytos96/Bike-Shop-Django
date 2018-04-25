from decimal import Decimal
from django.conf import settings
from bikes.models import Bike


class Cart(object):

    def __init__(self, request):
        """
        Initialize the cart.
        """
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # save an empty cart in the session
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def __len__(self):
        """
        Count all items in the cart.
        """
        return sum(item['quantity'] for item in self.cart.values())

    def __iter__(self):
        """
        Iterate over the items in the cart and get the books from the database.
        """
        bike_ids = self.cart.keys()
        # get the book objects and add them to the cart
        bikes = Bike.objects.filter(id__in = bike_ids)
        for bike in bikes:
            self.cart[str(bike.id)]['bike'] = bike

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def add(self, bike, quantity=1, update_quantity=False):
        """
        Add a book to the cart or update its quantity.
        """
        bike_id = str(bike.id)
        if bike_id not in self.cart:
            self.cart[bike_id] = {'quantity': 0,
                                      'price': str(bike.price)}
        if update_quantity:
            self.cart[bike_id]['quantity'] = quantity
        else:
            self.cart[bike_id]['quantity'] += quantity
        self.save()

    def remove(self, bike):
        """
        Remove a book from the cart.
        """
        bike_id = str(bike.id)
        if bike_id in self.cart:
            del self.cart[bike_id]
            self.save()

    def save(self):
        # update the session cart
        self.session[settings.CART_SESSION_ID] = self.cart
        # mark the session as "modified" to make sure it is saved
        self.session.modified = True

    def clear(self):
        # empty cart
        self.session[settings.CART_SESSION_ID] = {}
        self.session.modified = True

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())
