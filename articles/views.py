from django.shortcuts import render, redirect
from django.http import Http404, HttpResponseRedirect
from . models import Article, Picture, Category, Like, Dislike
from menu.models import Menu
from comments.models import Comment
from slider.models import Slider
from django.contrib.auth import get_user_model
from django.utils.html import strip_tags
from django.contrib.auth.decorators import login_required
from django.urls import reverse


User = get_user_model()


def homeview(request):
    menu_list = Menu.objects.all()
    sliders = Slider.objects.all()
    categories = Category.objects.all()
    articles = Article.objects.order_by('-pub_date').filter(published=True)[:10]
    context = {
        'categories':categories,
        'articles':articles,
        'sliders':sliders,
        'menu_list':menu_list,
    }
    return render(request, 'base.html', context)

def detailview(request, id):
    menu_list = Menu.objects.all()
    try:
        article = Article.objects.get(id=id)
    except Article.DoesNotExist():
        raise Http404('the article you are requesting is no longer available')
    pictures = Picture.objects.filter(article_id=id)
    comments = article.comment_set.all()
    categories = Category.objects.all()
    if request.user.is_authenticated:
        like = Like.objects.filter(article_id=id, user_id=request.user.id)
        dislike = Dislike.objects.filter(article_id=id, user_id=request.user.id)
    else:
        like="nolike";
        dislike = "nodislike";
    context = {
        'article':article,
        'pictures':pictures,
        'comments':comments,
        'categories':categories,
        'like':like,
        'dislike':dislike,
        'menu_list':menu_list,
    }
    
    return render(request, 'detail.html', context)

def searchview(request):
    menu_list = Menu.objects.all()
    categories = Category.objects.all()
    searchtext = request.POST['text']
    searchtext = strip_tags(searchtext)
    select = request.POST['select']
    searchtext = searchtext[:20]
    warning = "wrong search. Make sure you entered more than 2 symbols, and no html tags"
    
   
    if len(searchtext)>=3:
        if select=="articles":
            searchresult = Article.objects.filter(text__icontains=searchtext)
            res = 1
            
        elif select=="comments":
            searchresult = Comment.objects.filter(text__icontains=searchtext)
            res = 2
            
        elif select=="users":
            searchresult = User.objects.filter(username__icontains=searchtext)
            res = 3
            
    else:
        searchresult = ''
        select=warning
        res = 0
        
     
    context ={
            'searchresult':searchresult,
            'select':select,
            'res':res,
            'categories':categories,
            'menu_list':menu_list,
            }
    print(searchresult)
    return render(request, 'searchresult.html', context)

@login_required
def a_go_update(request, article_id):
    article = Article.objects.get(id=article_id)
    categories = Category.objects.all()
    context = {
        'article':article,
        'categories':categories,
    }
    return render(request, 'a_go_update.html', context)


@login_required
def a_update(request, article_id):
    menu_list = Menu.objects.all()
    article = Article.objects.get(id=article_id)
    check = request.FILES.get('picture')
    if check:
        article.image = request.FILES.get('picture')
   
    article.title=strip_tags(request.POST['title'])
    article.title=article.title[:100]
    
    article.text=strip_tags(request.POST['text'])
    article.text=article.text[:10000]
    article.save()
    
    context = {
        'article':article,
        'menu_list':menu_list,
    }
    return HttpResponseRedirect(reverse('articles:detailview', args=(article.id,)))


@login_required
def a_delete(request, article_id):
    article = Article.objects.get(id=article_id)
    article.delete()
    context = {
        'article':article,
    }
    return redirect('accounts:profile')


@login_required
def create_article(request):
    categories = Category.objects.all()
    context = {
        'categories':categories,
    }
    return render(request, 'create_article.html', context)


@login_required
def a_create(request):
    image = request.FILES['image']
    title = request.POST['title']
    text = request.POST['text']
    category = request.POST['select']
    usr = request.POST['usr']
    article = Article(title=title, text=text, category_id=category, author_id=usr, image=image)
    article.save()
    
    context = {
        'article':article,
    }
    return redirect('accounts:profile')


@login_required
def like(request, article_id):
    user_id = request.user.id
    check_like = Like.objects.filter(article_id=article_id, user_id=user_id)
    check_dislike = Dislike.objects.filter(article_id=article_id, user_id=user_id)

    if not check_like:
        l = Like.objects.create(article_id=article_id, user_id=user_id)
        l.save()
        if check_dislike:
            check_dislike.delete()
    else:
        check_like.delete()
            
        
    return HttpResponseRedirect(reverse('articles:detailview', args=(article_id,)))

@login_required
def dislike(request, article_id):
    user_id = request.user.id
    check_dislike = Dislike.objects.filter(article_id=article_id, user_id=user_id)
    check_like = Like.objects.filter(article_id=article_id, user_id=user_id)

    if not check_dislike:
        d = Dislike.objects.create(article_id=article_id, user_id=user_id)
        d.save()
        if check_like:
            check_like.delete()
    else:
        check_dislike.delete()
        
    return HttpResponseRedirect(reverse('articles:detailview', args=(article_id,)))


def catview(request, cat_id):
    menu_list = Menu.objects.all()
    categories = Category.objects.all() 
    category = Category.objects.get(id=cat_id)
    cat_article_list = Article.objects.filter(category_id=cat_id, published=True)

    context={
        'categories':categories,
        'category':category,
        'cat_article_list':cat_article_list,
        'menu_list':menu_list,
    }
    return render(request, 'category.html', context)

@login_required
def add_pic_view(request, article_id):
    menu_list = Menu.objects.all()
    article = Article.objects.get(id=article_id)
    
    context = {
        'article':article,
        'menu_list':menu_list,
    }
    return render(request, 'addpicture.html', context)

@login_required
def delete_pic_view(request, picture_id):
    picture = Picture.objects.get(id=picture_id)
    picture.delete()

    context = {
        'picture':picture,
    }
    return redirect('accounts:detailview')

@login_required
def add_pic_view_2(request, article_id):
    article = Article.objects.get(id=article_id)
    alt = request.POST['alt']
    picture = request.FILES['picture']
    p = Picture(alt=alt, picture=picture, article_id=article_id)
    p.save()

    return HttpResponseRedirect(reverse('articles:detailview', args=(article_id,)))
    

def menuitemview(request, item_id):
    categories = Category.objects.all()
    menu_list = Menu.objects.all()
    item = Menu.objects.get(id=item_id)
    context = {
        'item':item,
        'menu_list':menu_list,
        'categories':categories,
    }
    return render(request, 'menu_item.html', context)