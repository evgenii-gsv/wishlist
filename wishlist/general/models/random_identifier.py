from django.db import models
from django_extensions.db.fields import RandomCharField


class RandomIdentifierModel(models.Model):
    """Abstract model with RandomCharField identifier."""

    identifier = RandomCharField(length=8, editable=False, unique=True, db_index=True)  # type: ignore

    class Meta:
        abstract = True
