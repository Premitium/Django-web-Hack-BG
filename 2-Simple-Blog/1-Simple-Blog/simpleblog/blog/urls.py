from django.conf.urls import url

from .views import index, create_blog_post, login_view, profile_view, single_post, register_new_account, logout_view


urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^login/$', login_view, name='login'),
    url(r'^logout/$', logout_view, name='logout'),
    url(r'^profile/$', profile_view, name='profile'),
    url(r'^create/$', create_blog_post, name='create'),
    url(r'^register/$', register_new_account, name='register'),
    url(r'^single-post/(?P<id>[0-9]+)/$', single_post, name='single-post')
]
