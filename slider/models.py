from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from ckeditor.fields import RichTextField
from django.contrib.auth import get_user_model


class Slider(models.Model):
    title = models.CharField(max_length=50, default="this is title")
    text = models.CharField(max_length=255, default="slide image must be width:950px to height:450px")
    pub_date = models.DateField(auto_now_add=True)
    slide_image = models.ImageField(upload_to='slider/', blank=True)
    thumbnail = ImageSpecField(source='slide_image',
                               processors=[ResizeToFill(350, 220)],
                               format='JPEG',
                               options={'quality': 80})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'slider'
        verbose_name_plural = 'sliders'