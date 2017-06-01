from django.db import models

class BlogPostQuerySet(models.QuerySet):
    # def all(self, *args, **kwargs):
    #     return super(BlogPostManager, self).filter(is_private=False)

    def get_public_posts(self):
        return self.filter(is_private=False)

    def get_private_posts(self):
        return self.filter(is_private=True)

#python manage.py shell
#from blog.models.py import BlogPost, Tag
#QuerySets are quering the database for some sort of data
#If you want case insensitive QuerySet BlogPost.objects.filter(title__icontains="abc")
#QuerySet filters
#Model manager
