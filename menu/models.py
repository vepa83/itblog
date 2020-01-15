from django.db import models


class Menu(models.Model):
    title = models.CharField(max_length=50)
    is_category = models.BooleanField(default=False)

   
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'menu'
        verbose_name_plural = 'menues'