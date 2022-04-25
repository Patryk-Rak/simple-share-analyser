from django.db import models
from datetime import datetime, date


TYPE_OF_TRADE = (
        ('Sold', 'Sold'),
        ('Bought', 'Bought'),
    )

class Share(models.Model):
    name = models.CharField(max_length=200)
    amount = models.IntegerField()
    price = models.IntegerField()
    transaction_date = models.DateTimeField(default=datetime.now)
    type_of_trade = models.CharField(max_length=6, choices=TYPE_OF_TRADE)


    def __str__(self):
        return self.name

    @property
    def price_per_bulk(self):
        price_per_one = self.price / self.amount
        return price_per_one
