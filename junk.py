__author__ = 'jacob'
def compare_words(url):
        wordlist_query = []
        letters = []
        tot_length = len(url)
        i = 0
        decreasing = tot_length
        last_word = ""
        word_ins = None
        while i < tot_length:
            wordlist_query = WordList.objects.filter(usage=False, word__exact=url[i:tot_length])
            if wordlist_query:
                word = WordList.objects.get(pk=wordlist_query[0].pk)
                if len(word.word) > len(last_word):
                    last_word = word.word
                    word_ins = word
            i += 1

        return word_ins

def find_word(wordlist_query, url, iteration):
    """
    :param wordlist_query: queryset of the filtered wordlist
    :param url: either netloc or path (cleaned with regex)
    :param iteration: true if checking netloc, otherwise false. If false and no word was found, renew the oldest URL
    :return:
    """
    for w in wordlist_query:
        w = WordList.objects.get(pk=w.pk)
        if re.match(w.word, url):
            return w

    if not iteration:
        try:
            random_word_query = WordList.objects.filter(usage=False)
            qs = random_word_query[random.randint(0, random_word_query.count())]
            return WordList.objects.get(pk=qs.pk)
        except:
            #renew_oldest_url()  # function that renews the oldest url and set it to the new one
            return "Need to renew an old URL"
