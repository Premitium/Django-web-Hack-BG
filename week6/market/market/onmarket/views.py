from django.shortcuts import render
from django.http import HttpResponse

from .models import MarketCategory, MarketOffer

def index(request):

    offer = MarketOffer.objects.all();

    return render(request, 'onmarket/index.html', locals())
