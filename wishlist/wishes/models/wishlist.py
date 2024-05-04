from django.conf import settings
from django.db import models

from wishlist.general.models import RandomIdentifierModel, TimestampedModel


class Wishlist(TimestampedModel, RandomIdentifierModel):  # type: ignore
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='wishlists')
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    event_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name
