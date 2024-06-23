from django.db import models
from datetime import datetime, date

# Create your models here.



class Paper(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to="images", null=True)
    description = models.TextField(max_length=400)
    content = models.FileField(upload_to="papers", null=True)
    date = models.DateField(auto_now_add=True)
    
    slug = models.SlugField(max_length=200, default="", null=False)
    
    def __str__(self) -> str:
        return self.title

