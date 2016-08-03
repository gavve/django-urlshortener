from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver




class WordList(models.Model):
    word = models.CharField(max_length=200)
    usage = models.BooleanField(default=False)
    length = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["-length"]

    def __str__(self):
        return self.word

    def save(self, *args, **kwargs):
        if not self.id:
            self.length = len(self.word)
        super(WordList, self).save(*args, **kwargs)

class Url(models.Model):
    # Shorten and long URls
    short_url = models.URLField(verbose_name="Short Url", blank=True)
    long_url = models.URLField()

    word = models.ForeignKey(WordList)

    # Meta info
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-date_created"]

    def __str__(self):
        return self.short_url



@receiver(pre_delete, sender=Url)
def _mymodel_delete(sender, instance, **kwargs):
    # If one or multiple Urls are deleted it changes the status of the used Word
    # so that we can use it again for another short Url.
    instance.word.usage = False
    instance.word.save()
