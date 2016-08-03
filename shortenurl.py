__author__ = 'jacob'
from urlparse import urlparse
import re
import random
from urlshortener.models import Url, WordList

def process_url(long_url):
    tmp_url = long_url  # temporary hold the url

    url_parse = urlparse(tmp_url)  # parse URL, .netloc="www.google.se" .path="/search/python.html"

    clean_path = re.sub(r'[^a-zA-Z0-9/]+', '', url_parse.path)
    clean_path = re.sub(r'(-)', ' ', clean_path)
    complete_url = url_parse.netloc + clean_path

    word_ins = search(complete_url, len(complete_url))

    return word_ins


def search(url, max_length):
    queue = []
    i = 0
    for e in url:
        words = WordList.objects.filter(word__startswith=e, length__lte=max_length-i)
        queue.extend(words)
        i += 1

    for word in queue:
        if not word.usage:
            match = re.search(r'\b'+word.word+r'\b', url)
        if match:
            print "matcha ord: " + word.word

            return word

    return get_random_word(url)


def get_random_word(url):
    word = WordList.objects.filter(usage=False).order_by("?").first()
    if word:
        return word
    else:
        url = Url.objects.all().order_by('date_created')[0]  # get the oldest shorten Url
        word = WordList.objects.get(word=url.word)
        url.delete()  # using signals, so word will be usage=False after delete or url
        return word