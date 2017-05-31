from django.conf.urls import url
from django.contrib.auth.views import login, logout
from rest_framework_jwt.views import obtain_jwt_token
from .views import AddOfferCreateView, EditOfferUpdateView, OfferListView, DeleteOfferView, GetStatisticsView, PendingView, ApprovedAndRejectedOffers

urlpatterns = [
    url(r'^$', OfferListView.as_view(), name='index'),
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout, {'next_page': '/'}, name='logout'),
    url(r'^add-offer/$', AddOfferCreateView.as_view(), name='add-offer'),
    url(r'^offer/edit/(?P<pk>[0-9]+)', EditOfferUpdateView.as_view(), name='edit-offer'),
    url(r'^delete/(?P<pk>[0-9]+)$', DeleteOfferView.as_view(), name='delete-offer'),
    url(r'^statistics/$', GetStatisticsView.as_view(), name='statistics'),
    url(r'^pending/$', PendingView.as_view(), name='pending'),
    url(r'^approved-rejected/$', ApprovedAndRejectedOffers.as_view(), name='approved-rejected'),
    url(r'^api-token-auth/', obtain_jwt_token , name='drf_tocken'),
]
