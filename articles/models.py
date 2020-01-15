from django.db import models
from django.utils import timezone
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from ckeditor.fields import RichTextField
from django.contrib.auth import get_user_model

User = get_user_model()

class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'


class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    published = models.BooleanField(default=False)
    title = models.CharField(max_length=200)
    text = models.TextField(max_length=10000)
#    text = RichTextField()
    pub_date = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='article/', blank=True)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    thumbnail = ImageSpecField(source='image',
                               processors=[ResizeToFill(120, 120)],
                               format='JPEG',
                               options={'quality': 80})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'article'
        verbose_name_plural = 'articles'


class Picture(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    alt = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='article/pictures/', blank=True)
    thumbnail = ImageSpecField(source='picture', processors=[ResizeToFill(120, 120)], format='JPEG', options={'quality': 80})

    def __str__(self):
        return self.alt

    class Meta:
        verbose_name = 'article picture'
        verbose_name_plural = 'article pictures'

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.article.title

    class Meta:
        verbose_name = 'like'
        verbose_name_plural = 'likes'


class Dislike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=2)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, default=2)

    def __str__(self):
        return self.article.title

    class Meta:
        verbose_name = 'dislike'
        verbose_name_plural = 'dislikes'





