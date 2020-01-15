from django.db import models
from articles.models import Article
from django.contrib.auth import get_user_model

User = get_user_model()


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=2)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    text = models.TextField(max_length=1000)
    pub_date = models.DateTimeField(auto_now_add=True)
    like = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)

    def __str__(self):
        return self.text[:15]

    class Meta:
        verbose_name = 'comment'
        verbose_name_plural = 'comments'