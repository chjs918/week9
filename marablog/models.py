from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

# Create your models here.
class Mara(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    score_Choices = (
        ('★','★'),
        ('★★','★★'),
        ('★★★','★★★'),
        ('★★★★','★★★★'),
        ('★★★★★','★★★★★'),
    )
    score = models.TextField(choices=score_Choices)
    writer = models.CharField(max_length=100)
    img = models.ImageField(upload_to="mara/", blank = True, null = True)
    image_thumbnail = ImageSpecField(source = 'img', processors=[ResizeToFill(120,100)])

    def __str__(self):
          return self.title

    def summary(self):
        return self.content[:50]