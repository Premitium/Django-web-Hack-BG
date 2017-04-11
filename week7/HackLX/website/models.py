from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Offer(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    category = models.ForeignKey(Category)
    author = models.ForeignKey(User)

    image = models.ImageField()

    def __str__(self):
        return self.title
