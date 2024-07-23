from django.db import models
from datetime import date
from django_ckeditor_5.fields import CKEditor5Field

# Create your models here.



class Paper(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to="images", null=True)
    description = models.TextField(max_length=400, null=True)
    content = models.FileField(upload_to="papers", null=True)
    date = models.DateField(default=date.today)
    
    slug = models.SlugField(max_length=200, default="", null=False)
    
    def __str__(self) -> str:
        return self.title

