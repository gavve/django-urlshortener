from django.shortcuts import render, HttpResponseRedirect, get_object_or_404, redirect
from fyndiq.settings import SHORT_URL_BASE
# Create your views here.
# Forms
from .forms import UrlForm

# Scripts
from shortenurl import process_url

# Models
from .models import Url

def index(request):
    return render(request, "urlshortener/base.html", {'urlForm': UrlForm})


def generate_short_url(request):
    short_url = ""
    if request.method == "POST":
        # make an instance of the form
        form = UrlForm(request.POST)
        # check if form is valid
        if form.is_valid():
            # start processing the url
            url = form.cleaned_data['long_url']
            if Url.objects.filter(long_url=url).exists():
                short_url = Url.objects.get(long_url=url).short_url
                c = {
                    'urlExists': url,
                     'short_url': short_url,
                     'urlForm': UrlForm
                }

            else:
                word = process_url(url)  # returns dict {'short': url str, 'word': instance}
                short_url = SHORT_URL_BASE + word.word

                new_url = Url(short_url=short_url, long_url=url, word=word)  # save the short URL
                word.usage = True  # sets word to used
                word.save()
                new_url.save()
                form.save(commit=False)
                c = {
                    'success': "Your new Shorten URL is: ",
                    'short_url': short_url,
                }

    else:
        c = {'fail': "Something went wrong"}
        return HttpResponseRedirect('/')

    return render(request, "urlshortener/base.html", c)


def redirect_to_long_url(request, short_url):
    url = get_object_or_404(Url, short_url=SHORT_URL_BASE+short_url)
    return redirect(url.long_url)
