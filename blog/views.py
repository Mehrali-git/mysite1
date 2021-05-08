from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.http import HttpResponse, Http404
from django.template import loader
from . import models
from django.core.paginator import Paginator


class ArticleList(ListView):
    queryset = models.Articles.objects.published()
    paginate_by = 3


# def detail(request, slug):
#     context = {
#         'article': get_object_or_404(models.Articles, slug=slug),
#         # 'category':models.Category.objects.filter(status=True)
#     }
#     return render(request, "blog/articles_detail.html", context)
class ArticleDetail(DetailView):
    def get_object(self, queryset=None):
        slug = self.kwargs.get('slug')
        return get_object_or_404(models.Articles, slug=slug)


#
# def category(request, slug, page=1):
#     category = get_object_or_404(models.Category, slug=slug, status=True)
#     article_list = category.articles.published()
#     paging = Paginator(article_list, 4)
#     list_data = paging.get_page(page)
#     context = {
#         'category': category,
#         'articles': list_data,
#     }
#     return render(request, "blog/category_list.html", context)
class CategoryList(ListView):
    template_name = 'blog/category_list.html'
    paginate_by = 2

    def get_queryset(self):
        global category
        slug = self.kwargs.get('slug')
        category = get_object_or_404(models.Category.object.active(), slug=slug)
        return category.articles.published()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = category
        return context


class CategoryList(ListView):
    template_name = 'blog/category_list.html'
    paginate_by = 2

    def get_queryset(self):
        global category
        slug = self.kwargs.get('slug')
        category = get_object_or_404(models.Category.object.active(), slug=slug)
        return category.articles.published()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = category
        return context


class AuthorList(ListView):
    template_name = 'blog/author_list.html'
    # paginate_by = 2

    def get_queryset(self):
        global author
        username = self.kwargs.get('username')
        author = get_object_or_404(User, username=username)
        return author.articles.published()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author'] = author
        return context
