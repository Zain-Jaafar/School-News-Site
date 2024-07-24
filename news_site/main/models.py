from django.db import models
from datetime import date

# Create your models here.


# This model is for adding newspapers to the database
class Paper(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to="images", null=True)
    description = models.TextField(max_length=400, null=True)
    content = models.FileField(upload_to="papers", null=True)
    date = models.DateField(default=date.today)
    
    slug = models.SlugField(max_length=200, default="", null=False)
    
    
    '''
    This function makes it so that when you check the list of papers in the 
    admin panel, you see the title of the paper, instead of Paper(0), Paper(1), Paper(2) etc.
    '''
    def __str__(self) -> str:
        return self.title

