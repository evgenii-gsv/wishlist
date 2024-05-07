from django.db import models


class TimestampedModel(models.Model):
    """Abstract model with created and modified fields."""

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
