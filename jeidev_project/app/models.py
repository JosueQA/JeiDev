from django.db import models
from django.urls import reverse

# Create your models here.
class AppModel(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    file = models.FileField(upload_to="apps/")
    description = models.TextField()
    hook = models.TextField(max_length=80)

    image = models.ImageField(upload_to="images/", blank=True, null=True)
    iframe = models.URLField(blank=True, null=True)

    @property
    def download_url(self):
        return reverse("app_download", args=[self.id])

    @property
    def app_link(self):
        return reverse("app", args=[self.slug])

    def __str__(self):
        return self.name
