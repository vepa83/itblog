from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse, HttpResponseRedirect
from . models import Comment
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from articles.models import Article
from django.contrib.auth import get_user_model
from django.utils.html import strip_tags

User = get_user_model()


@login_required
def leavecomment(request, article_id):
    user = request.user
    try:
        article = Article.objects.get(id=article_id)
    except Article.DoesNotExist():
        raise Http404('the article you are requesting is no longer available')
    article.comment_set.create(author_id=user.id, text=strip_tags(request.POST['text']))
    return HttpResponseRedirect(reverse('articles:detailview', args=(article.id,)))

@login_required
def deletecomment(request, comment_id):
    comment = Comment.objects.get(id=comment_id)
    comment.delete()
    context = {
        'comment':comment,
    }
    return redirect('accounts:profile')