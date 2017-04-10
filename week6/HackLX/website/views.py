from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy
from .models import Offer, Category

from django.views.generic.edit import FormView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views import View


def index(request):
    offers = Offer.objects.select_related('category', 'author').all()

    return render(request, 'website/index.html', locals())


class AddOfferCreateView(LoginRequiredMixin, CreateView):
    template_name = 'website/add_offer.html'
    success_url = reverse_lazy('website:index')
    model = Offer
    fields = ('title', 'description', 'category', 'image')
    import ipdb; ipdb.set_trace()

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(AddOfferCreateView, self).form_valid(form)

    def get_success_url(self):
        return success_url


@login_required(login_url='website:login')
def edit_offer(request, pk):
    offer = get_object_or_404(Offer, pk=int(pk))
    form = OfferCreateModelForm(instance=offer)

    if request.method == 'POST':
        form = OfferCreateModelForm(request.POST, request.FILES)

        if form.is_valid():
            form = form.save(commit=False)
            form.author = request.user
            form.save()
            return redirect(reverse('website:index'))

    return render(request, 'website/add_offer.html', locals())

def delete_offer(request, pk):
    offer = get_object_or_404(Offer, pk=int(pk))
    offer.delete()
    return redirect(reverse('website:index'))

def get_statistics(request):
    # TODO: Move logic in services
    categories = Category.objects.all()
    categories_result = {}

    for category in categories:
        categories_result[category.name] = category.offer_set.count()


    # TODO: Add more statistics information

    return render(request, 'website/statistics.html', locals())
