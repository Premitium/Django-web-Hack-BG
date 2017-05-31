from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy
from .models import Offer, Category
from django.views.generic import ListView
from django.views.generic.base import TemplateView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from . import services, mixins
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly


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

class PendingView(ListView):
    model = Offer
    template_name = 'website/pending_offer.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pending'] = services.get_offer_status_pending(Offer)
        return context

class ApprovedAndRejectedOffers(ListView):
    model = Offer
    template_name = 'website/approved_rejected_offer.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['approved_rejected'] = services.get_offer_status_approved_rejected(Offer)
        return context


#"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJlbWFpbCI6InNwLnBhcnZhbm92QGdtYWlsLmNvbSIsInVzZXJuYW1lIjoic2ltZW9ucGFydmFub3YiLCJleHAiOjE0OTI3MDk5OTl9.c7ff2-Tb-sEY7yHArniFd2Sm43ONS-bWrBHXyJ5XzuQ"
class PermissionGranted(APIView):
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get(self):
        pass

    def post(self):
        pass
