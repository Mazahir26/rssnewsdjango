from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE


# Create your models here.
class Feed(models.Model):
    name = models.CharField(max_length=50,null=False,unique=True)
    feed = models.URLField(unique=True,null=False)
    Users = models.ManyToManyField(User)
    Category = models.CharField(max_length=30,default="General")
    def __str__(self):
        return self.name

class SavedURL(models.Model):
    url = models.URLField(null=False)
    Users = models.ManyToManyField(User)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.url



