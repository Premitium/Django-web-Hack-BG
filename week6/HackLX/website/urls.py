from django.conf.urls import url
from django.contrib.auth.views import login, logout
from .views import index, edit_offer, delete_offer, get_statistics, AddOfferCreateView

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout, {'next_page': '/'}, name='logout'),
    url(r'^add-offer/$', AddOfferCreateView.as_view(), name='add-offer'),
    url(r'^offer/edit/(?P<pk>[0-9]+)', edit_offer, name='edit-offer'),
    url(r'^delete/(?P<pk>[0-9]+)$', delete_offer, name='delete-offer'),
    url(r'^statistics/$', get_statistics, name='statistics'),
]
