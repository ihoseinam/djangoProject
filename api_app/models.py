from django.db import models
from datetime import datetime


# Create your models here.
class Book(models.Model):
    name = models.CharField(null=True,max_length=150)
    store_name = models.CharField(null=True,max_length=50)
    description = models.TextField(null=True)
    image = models.ImageField(default='', upload_to='store_image/', null=True,blank=True)
    fave = models.BooleanField(default=False)
    create_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name
