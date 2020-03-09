from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from articles.models import Article, Picture, Category
from comments.models import Comment
from menu.models import Menu


@login_required
def ProfileView(request):
    menu_list = Menu.objects.all()
    categories = Category.objects.all()
    articles = Article.objects.filter(author_id=request.user.id).order_by('-pub_date')
    comments = Comment.objects.filter(author_id=request.user.id).order_by('-pub_date')
    
 
    context ={
        'articles':articles,
        'comments':comments,
        'categories':categories,
        'menu_list':menu_list,
    }
   
    return render(request, 'profile.html', context)


def RegisterView(request):
    menu_list = Menu.objects.all()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("accounts:login_url")
    else:
        form = UserCreationForm()
    context = {
        'form':form,
        'menu_list':menu_list,
    }
    return render(request, 'registration/register.html', context)

