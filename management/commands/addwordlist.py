__author__ = 'jacob'
from django.core.management.base import BaseCommand, CommandError
from urlshortener.models import WordList
import re


class Command(BaseCommand):
    help = 'Add words from textfile to WordList'

    def add_arguments(self, parser):
        parser.add_argument('filename', nargs='+', type=str)

    def handle(self, *args, **options):
        for filename in options['filename']:
            try:
                file = open(filename, 'r')
                for line in file:
                    word = line.lower()
                    word = re.sub(r'[^a-z0-9]+', '', word)
                    w = WordList.objects.filter(word=word)
                    if w:
                        w = WordList.objects.get(pk=w[0].pk)
                        self.stdout.write(self.style.SUCCESS('"%s" already existed in the wordbank. Continues to next word.' % w.word))
                    else:
                        w = WordList(word=word)
                        w.usage = False
                        w.save()
                        self.stdout.write(self.style.SUCCESS('Successfully added word "%s"' % w.word))
                file.close()
            except IOError:
                print "Cannot open %s" % filename
