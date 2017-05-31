from django.conf.urls import url

from .views import index, success_redirect_view, download_mp3

#uuid_pattern = '[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}'

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^success/$', success_redirect_view, name='success'),
    url(r'^download/(?P<filename>\w{0,50})/?', download_mp3, name='download_mp3')
]
