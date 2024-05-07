from django.db import models
from djmoney.models.fields import MoneyField

from wishlist.general.models import RandomIdentifierModel, TimestampedModel

from .wishlist import Wishlist


class Wish(TimestampedModel, RandomIdentifierModel):
    wishlist = models.ForeignKey(Wishlist, on_delete=models.CASCADE, related_name='wishes')
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    url = models.URLField()
    price = MoneyField(max_digits=14, decimal_places=2)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'wishes'
