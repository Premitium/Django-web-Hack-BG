from django.conf.urls import url

from .views import CreateCustomerView


urlpatterns = [
    url(
        regex='^payments$',
        view=CreateCustomerView.as_view(),
        name='paymentstripe'
    )
]
