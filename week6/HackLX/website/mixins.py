from django.contrib.auth.mixins import UserPassesTestMixin

class CanUpdateOfferMixin(UserPassesTestMixin):

    def test_func(self):
        #how do you get the urls kwargs
        offer_id = self.request.
