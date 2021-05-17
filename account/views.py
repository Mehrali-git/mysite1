from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.urls import reverse_lazy
from blog.models import Articles
from django.contrib.auth.views import LoginView, PasswordChangeView
from .mixins import FieldsMixin, FormValidMixin, AccessMixin, AuthorsAccessMixin
from .models import User
from .forms import ProfileForms


class ArticleList(LoginRequiredMixin, AuthorsAccessMixin, ListView):
    queryset = Articles.objects.all
    template_name = 'registration/home.html'

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Articles.objects.all
        else:
            return Articles.objects.filter(author=self.request.user)


class ArticleCreate(LoginRequiredMixin, AuthorsAccessMixin, FormValidMixin, FieldsMixin, CreateView):
    model = Articles
    template_name = 'registration/article-create-update.html'


class ArticleUpdate(AccessMixin, AuthorsAccessMixin, FieldsMixin, UpdateView):
    model = Articles
    template_name = 'registration/article-create-update.html'


class ArticleDelete(AccessMixin, AuthorsAccessMixin, DeleteView):
    model = Articles
    success_url = reverse_lazy("account:home")
    template_name = 'registration/articles_confirm_delete.html'


class Profile(LoginRequiredMixin, UpdateView):
    form_class = ProfileForms
    template_name = 'registration/profile.html'
    success_url = reverse_lazy('account:profile')

    def get_object(self, queryset=None):
        return User.objects.get(pk=self.request.user.pk)

    def get_form_kwargs(self):
        kwargs = super(Profile, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs


class Login(LoginView):
    def get_success_url(self):
        if self.request.user.is_superuser or self.request.user.is_author:
            return reverse_lazy('account:home')
        else:
            return reverse_lazy('account:profile')


class PasswordChange(PasswordChangeView):
    success_url = reverse_lazy('account:password_change_done')
