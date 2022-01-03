from django.db import models


CHAIN_HARMONY_ONE = 0
CHAIN_AVALANCHE = 1

CHAIN_CHOICES = [
    (CHAIN_HARMONY_ONE, 'Harmony one'),
    (CHAIN_AVALANCHE, 'Avalanche'),
]


class TokenPrice(models.Model):
    token = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    datetime = models.DateTimeField()
    price = models.DecimalField(max_digits=30, decimal_places=16)


class Token(models.Model):
    name = models.CharField(max_length=100)
    symbol = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    chain = models.IntegerField(default=0, choices=CHAIN_CHOICES)
    decimals = models.IntegerField()

    def __str__(self):
        return "%s %s" % (self.address, self.name)
