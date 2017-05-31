from django.contrib.auth.mixins import UserPassesTestMixin

class BaseUserPassesTestMixin(UserPassesTestMixin):
    def test_func(self):
        return True

class CanUpdateOfferMixin(BaseUserPassesTestMixin):
    raise_exception = True

    def test_func(self):
        offer_id = self.kwargs.get('offer')
        # self request user 
        import ipdb; ipdb.set_trace()
        # offer_id = self.request.kwarg


class IsSuperUserMixin(BaseUserPassesTestMixin):

    def test_func(self):
        import ipdb; ipdb.set_trace()
        #is_super
        # offer_id = self.request.
