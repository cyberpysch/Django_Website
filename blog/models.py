from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.
class blogPost(models.Model):
    sno=models.AutoField(primary_key=True)
    topic=models.CharField(max_length=100)
    title=models.CharField(max_length=100)
    timestamp=models.DateTimeField(blank=True)
    author=models.CharField(max_length=50)
    slug=models.CharField(max_length=200)
    content=models.TextField()

    def __str__(self):
        return self.title +" by "+self.author
    

   