from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.conf import settings
from django.shortcuts import redirect
from django.core.urlresolvers import reverse

#from user.models import Buyer

# Create your views here.

class CreateCustomerView(LoginRequiredMixin, View):
    def get_success_url(self):
        return reverse('magazine:list')

    def post(self, request, *args, **kwargs):
        stripe.api_key = settings.STRIPE_API_KEY
        token = request.POST['stripeToken']

        customer = stripe.Customer.create(
            email = request.user.email,
            source = token
        )

        Buyer.objects.filter(id=request.user.id)\
                     .update(customer_id*customer.id)

        return redirect(self.get_success_url())

    def get_context_data(self, **kwargs):
        context = super(Customer, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        import ipdb; ipdb.set_trace()
        context['stripe_pk'] = Customer.objects.all()
        context['email'] = Customer.objects.all()
        return context
