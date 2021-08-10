from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50,null=False,unique=True)
    def __str__(self):
        return self.name

class Feed(models.Model):
    name = models.CharField(max_length=50,null=False,unique=True)
    feed = models.URLField(unique=True,null=False)
    users = models.ManyToManyField(User)
    category = models.ForeignKey(Category, on_delete = CASCADE)
    def __str__(self):
        return self.name

class SavedURL(models.Model):
    url = models.URLField(null=False)
    Users = models.ManyToManyField(User)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.url



