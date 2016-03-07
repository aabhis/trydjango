from __future__ import unicode_literals

from django.db import models

# Create your models here.
class FilmLocations(models.Model):
    title = models.CharField(max_length=255,null=True)
    location = models.CharField(max_length=255,null=True)
    state = models.CharField(max_length=255,null=True)
    city = models.CharField(max_length=255,null=True)
    latitude = models.CharField(max_length=255,null=True)
    longitude = models.CharField(max_length=255,null=True)
    accuracyscore = models.CharField(max_length=255,null=True)
    accuracytype = models.CharField(max_length=255,null=True)
    number = models.CharField(max_length=255,null=True)
    street = models.CharField(max_length=255,null=True)
    city = models.CharField(max_length=255,null=True)
    state = models.CharField(max_length=255,null=True)
    county = models.CharField(max_length=255,null=True)
    zipcode = models.CharField(max_length=255,null=True)
    
    def __unicode__(self):
        return self.title