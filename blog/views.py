from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.http import HttpResponse, Http404
from django.template import loader
from django.contrib.auth.models import User
from . import models
from django.core.paginator import Paginator


# def home(request,page=1):
#     data=models.Articles.objects.published()
#     paging=Paginator(data,4)
#     # page=request.GET.get('page')
#     list_data=paging.get_page(page)
#     context={
#     'articles':list_data,
#     # 'category':models.Category.objects.filter(status=True)
#     }
# return render(request,"blog/home.html",context)

class ArticleList(ListView):
    # model=Articles
    # template_name="blog/home.html"
    # context_object_name="articles"
    queryset = models.Articles.objects.published()
    paginate_by = 4


# def detail(request,slug):
#         context={
#         'article':get_object_or_404(models.Articles,slug=slug),
#         # 'category':models.Category.objects.filter(status=True)
#         }
#         return render(request,"blog/detail.html",context)
class ArticleDetail(DetailView):
    def get_object(self):
        slug = self.kwargs.get('slug')
        return get_object_or_404(models.Articles.objects.published(), slug=slug)


# def category(request,slug,page=1):
#     category=get_object_or_404(models.Category.objects.active(),slug=slug)
#     article_list=category.articles.published()
#     paging=Paginator(article_list,4)
#     list_data=paging.get_page(page)
#     context={
#     'category':category,
#     'articles':list_data,
#     }
#     return render(request,"blog/category.html",context)

class CategoryList(ListView):
    paginate_by = 4
    template_name = 'blog/category_list.html'

    def get_queryset(self):
        global category
        slug = self.kwargs.get('slug')
        category = get_object_or_404(models.Category.objects.active(), slug=slug)
        return category.articles.published()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = category
        return context


# def author(request,username,page=1):
#     author=get_object_or_404(User,username=username)
#     article_list=author.articles.published()
#     paging=Paginator(article_list,4)
#     list_data=paging.get_page(page)
#     context={
#     'author':author,
#     'articles':list_data,
#     }
#     return render(request,"blog/author.html",context)

class AuthorList(ListView):
    paginate_by = 4
    template_name = 'blog/author_list.html'

    def get_queryset(self):
        global author
        username = self.kwargs.get('username')
        author = get_object_or_404(User, username=username)
        return author.articles.published()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author'] = author
        return context
