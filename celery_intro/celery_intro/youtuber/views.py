from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404, redirect
from .forms import SubmitForm
from .tasks import chain_tasks
from .models import AudioFile

def index(request):
    form = SubmitForm()
    if request.method == 'POST':
        form = SubmitForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data.get('url')
            to_email = form.cleaned_data.get('email')
            chain_tasks(url=url, email = to_email, host = request.get_host()).apply_async()
        else:
            return HttpResponseBadRequest('<h1>Something went wrong<br /></h1>')

        return redirect(reverse_lazy('youtuber:success'))
    return render(request, 'index.html', locals())

def success_redirect_view(request):
    return render(request, 'success.html', locals())

def download_mp3(request, filename):
    pass
