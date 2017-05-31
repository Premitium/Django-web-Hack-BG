from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Offer(models.Model):

    STATUS_CHOICES = (
        (1, 'PENDING'),
        (2, 'APPROVED'),
        (3, 'REJECTED'),
    )

    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    category = models.ForeignKey(Category)
    author = models.ForeignKey(User)
    status = models.SmallIntegerField(choices=STATUS_CHOICES, default=1)

    image = models.ImageField()

    def __str__(self):
        return self.title
