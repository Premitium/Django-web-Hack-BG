from django.conf.urls import url
from django.contrib.auth.views import login, logout
from .views import get_statistics, AddOfferCreateView, EditOfferUpdateView, OfferListView, DeleteOfferView

urlpatterns = [
    url(r'^$', OfferListView.as_view(), name='index'),
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout, {'next_page': '/'}, name='logout'),
    url(r'^add-offer/$', AddOfferCreateView.as_view(), name='add-offer'),
    url(r'^offer/edit/(?P<pk>[0-9]+)', EditOfferUpdateView.as_view(), name='edit-offer'),
    url(r'^delete/(?P<pk>[0-9]+)$', DeleteOfferView.as_view(), name='delete-offer'),
    url(r'^statistics/$', get_statistics, name='statistics'),
]
