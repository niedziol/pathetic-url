from django.http import HttpResponsePermanentRedirect
from django.shortcuts import render, get_object_or_404

from .forms import ShortUrlForm
from .models import Url
from pathetic.base import base_decode, base_encode
from django.db.models import F


def index(request):
    if request.method == "POST":
        form = ShortUrlForm(request.POST)
        if form.is_valid():
            url = form.save()
            return render(request, 'path/show_url.html', {'short_url': base_encode(url.id)})
    else:
        form = ShortUrlForm()
    return render(request, 'path/index.html', {'form': form})


def redirect(request, short_url):
    link = get_object_or_404(Url, id=base_decode(short_url))
    link.visited += F('visited') + 1
    link.save()
    return HttpResponsePermanentRedirect(link.long_url)
