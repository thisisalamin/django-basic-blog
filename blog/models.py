from django.db import models
from datetime import datetime

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=250)
    descriptions = models.TextField()
    publish = models.DateTimeField('published',default=datetime.now())

    def __str__(self):
        return self.title
    
    