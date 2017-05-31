from django.conf.urls import url, include

#1.http://127.0.0.1:8000/api/storage/create-user/
#12597158-9a19-4c46-aa90-7f4f28beda57
from .views import create_user_view, store_data_view, manage_key_view

uuid_regex = '([a-zA-Z]|[0-9]){8}\-([a-zA-Z]|[0-9]){4}\-([a-zA-Z]|[0-9]){4}\-([a-zA-Z]|[0-9]){4}\-([a-zA-Z]|[0-9]){12}'

storage_patterns = [
    url(r'^create-user/$', create_user_view),
    url(r'^(?P<identifier>{})/$'.format(uuid_regex), store_data_view),
    url(r'^(?P<identifier>{})/(?P<key>.*)/$'.format(uuid_regex), manage_key_view),
]

urlpatterns = [
    url(r'^storage/', include(storage_patterns))
]
