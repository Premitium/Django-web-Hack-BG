from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy
from .models import Offer, Category
from django.views.generic import ListView
from django.views.generic.base import TemplateView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from . import services


class OfferListView(ListView):
    model = Offer

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['categories'] = Category.objects.count()

        return context

class AddOfferCreateView(LoginRequiredMixin, CreateView):
    template_name = 'website/add_offer.html'
    success_url = reverse_lazy('website:index')
    model = Offer
    fields = ('title', 'description', 'category', 'image')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(AddOfferCreateView, self).form_valid(form)

    def get_success_url(self):
        return self.success_url


class EditOfferUpdateView(LoginRequiredMixin, UpdateView):
    model = Offer
    fields = ('title', 'description', 'category', 'image')
    template_name = 'website/add_offer.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('website:index')


class DeleteOfferView(LoginRequiredMixin, DeleteView):
    model = Offer
    template_name = 'website/delete_offer.html'

    def get_success_url(self):
        return reverse_lazy('website:index')

class GetStatisticsView(LoginRequiredMixin, TemplateView):
    model = Offer
    template_name = 'website/statistics.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.count()
        context['titles'] = services.get_categoty_names(Category)
        return context
