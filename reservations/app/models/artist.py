from django.db import models

class Artist (models.Model):
    """model definition Artist"""

    firstname= models.CharField(max_length = 60)
    lastname = models.CharField(max_length = 60)
