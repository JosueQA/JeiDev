from django.db import models
from django.utils.text import slugify

# Create your models here.
class AppModel(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField()



    def __str__(self):
        return self.name