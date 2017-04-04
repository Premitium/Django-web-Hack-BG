from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

import moneyed
from djmoney.models.fields import MoneyField
# Create your models here.

class MarketCategory(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class MarketOffer(models.Model):
    item_name = models.CharField(max_length=255)
    price = MoneyField(max_digits=10, decimal_places=2, default_currency='USD')
    authors = models.ManyToManyField(User, related_name='author')
    created_at = models.DateTimeField(default=timezone.now)
    content = models.TextField()

    def __str__(self):
        return self.item_name
