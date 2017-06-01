from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from .managers import BlogPostQuerySet

class Tag(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class BlogPost(models.Model):
    title = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.TextField()
    authors = models.ManyToManyField(User, related_name='author')
    tags = models.ManyToManyField(Tag, related_name='posts')
    is_private = models.BooleanField(default=False)

    #filter all posts based on their fields
    objects = BlogPostQuerySet.as_manager()


    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()

        super().save(*args, **kwargs)

class CommentAuthor(models.Model):
    email = models.EmailField()
    full_name = models.CharField(max_length=255)

class Comment(models.Model):
    author = models.ForeignKey(CommentAuthor, related_name='comments', null=True)
    content = models.TextField()
    blogpost = models.ForeignKey(BlogPost, related_name='comments')
