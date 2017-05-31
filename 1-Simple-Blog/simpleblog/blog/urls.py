from django.conf.urls import url

from .views import index, create_blog_post, login_view, profile_view, detail_post_view


urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^login/$', login_view, name='login'),
    url(r'^profile/$', profile_view, name='profile'),
    url(r'^create/$', create_blog_post, name='create'),
    url(r'^blog_post/(?P<blog_post_id>[0-9]+)$', detail_post_view, name='blog_post_detail')
]

#  url(r'^articles/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<day>[0-9]{2})/$',
# A request to /articles/2003/03/03/ would call the function views.article_detail(request, year='2003', month='03', day=’03')
