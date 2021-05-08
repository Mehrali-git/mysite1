from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404
from django.template import loader
from django.contrib.auth.models import User
from . import models
from django.core.paginator import Paginator

def home(request,page=1):
    data=models.Articles.objects.published()
    paging=Paginator(data,4)
    # page=request.GET.get('page')
    list_data=paging.get_page(page)
    context={
    'articles':list_data,
    # 'category':models.Category.objects.filter(status=True)
    }
    return render(request,"blog/home.html",context)
def detail(request,slug):
        context={
        'article':get_object_or_404(models.Articles,slug=slug),
        # 'category':models.Category.objects.filter(status=True)
        }
        return render(request,"blog/detail.html",context)
def category(request,slug,page=1):
    category=get_object_or_404(models.Category.objects.active(),slug=slug)
    article_list=category.articles.published()
    paging=Paginator(article_list,4)
    list_data=paging.get_page(page)
    context={
    'category':category,
    'articles':list_data,
    }
    return render(request,"blog/category.html",context)
def author(request,username,page=1):
    author=get_object_or_404(User,username=username)
    article_list=author.articles.published()
    paging=Paginator(article_list,4)
    list_data=paging.get_page(page)
    context={
    'author':author,
    'articles':list_data,
    }
    return render(request,"blog/author.html",context)
