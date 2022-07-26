from PIL import Image as Im
from django.db import models

# Create your models here.

class Image(models.Model):
    imageName = models.CharField(max_length=100)
    imageUrl = models.ImageField(upload_to='image-files')
    imageDetails = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.imageName} image'

    def save(self, *args, **kwargs):
        super(Image, self).save(*args, **kwargs)