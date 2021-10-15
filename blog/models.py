from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ManyToManyField
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class posts(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=100)
    puplished = models.TimeField(default=timezone.now)
    img = models.ImageField(upload_to='posts/')

    def __str__(self):
        return self.title


class comments(models.Model):
    post = models.ForeignKey(posts, on_delete=models.CASCADE)
    author = models.ForeignKey(User,related_name='auth_comment',on_delete=CASCADE)
    text = models.TextField(max_length=200)

    def __str__(self):
        return str(self.post)
    
