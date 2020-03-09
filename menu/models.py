from django.db import models
from articles.models import Category

class Menu(models.Model):
    title = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)

   
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'menu'
        verbose_name_plural = 'menues'