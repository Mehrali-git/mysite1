from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView
from blog.models import Articles
from .mixins import FieldsMixin, FormValidMixin, AccessMixin


class ArticleList(LoginRequiredMixin, ListView):
    queryset = Articles.objects.all
    template_name = 'registration/home.html'

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Articles.objects.all
        else:
            return Articles.objects.filter(author=self.request.user)


class ArticleCreate(LoginRequiredMixin, FieldsMixin, CreateView):
    model = Articles
    template_name = 'registration/article-create-update.html'


class ArticleUpdate(AccessMixin, FieldsMixin, UpdateView):
    model = Articles
    template_name = 'registration/article-create-update.html'
