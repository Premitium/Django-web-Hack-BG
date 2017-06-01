from .models import BlogPost, Tag


def create_blog_post(*,
                     title,
                     content,
                     is_private,
                     tags=None):
    errors = []

    if not title.strip():
        errors.append('Title is required.')

    if not content.strip():
        errors.append('Content is required.')

    if errors:
        return None, errors

    post = BlogPost.objects.create(title=title, content=content, is_private=is_private)

    for tag in Tag.objects.filter(id__in=tags):
        post.tags.add(tag)

    post.save()

    return post, None

def get_all_blogs():
    return list(BlogPost.objects.get_public_posts())


def get_private_posts():
    return list(BlogPost.objects.get_private_posts())
