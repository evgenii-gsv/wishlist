from typing import List

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from wishlist.general.models import RandomIdentifierModel

from ..managers import UserManager


class User(AbstractUser, RandomIdentifierModel):
    username = None
    first_name = None
    last_name = None
    email = models.EmailField(_('email address'), unique=True)
    name = models.CharField(_('name'), max_length=255, null=True, blank=True)
    date_of_birth = models.DateField(_('date of birth'), null=True, blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS: List[str] = []
