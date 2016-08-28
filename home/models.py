from __future__ import unicode_literals

from django.db import models


class Language(models.Model):
    name = models.CharField(max_length=20)

    def __unicode__(self):
        return self.name


class Function(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField(max_length=200)
    date = models.DateTimeField()
    language = models.ForeignKey(Language)

    def __unicode__(self):
        return self.title
