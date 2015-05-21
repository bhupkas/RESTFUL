from django.db import models

# Create your models here.

class Profile(models.Model):
    name = models.CharField(max_length=200)
    phone = models.IntegerField()

    def __unicode__(self):
    	return self.name
