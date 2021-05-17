from django.http import Http404
from django.shortcuts import get_object_or_404, redirect
from blog.models import Articles


class FieldsMixin():
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser:
            self.fields = ["author", "title", "category", "slug", "description", "thamnail", "publish",
                           "status", "is_special"]
        elif request.user.is_author:
            self.fields = ["title", "category", "slug", "description", "thamnail", "publish", "is_special"]
        else:
            raise Http404("شما امکان دسترسی به این صفحه را ندارید")
        return super().dispatch(request, *args, **kwargs)


class FormValidMixin():
    def form_valid(self, form):
        if self.request.user.is_superuser:
            form.save()
        else:
            self.obj = form.save(commit=False)
            self.obj.author = self.request.user
            self.obj.status = 'd'
        return super().form_valid(form)


class AccessMixin():
    def dispatch(self, request, pk, *args, **kwargs):
        articles = get_object_or_404(Articles, pk=pk)
        if articles.author == request.user and articles.status == 'd' or request.user.is_superuser:
            return super().dispatch(request, pk, *args, **kwargs)
        else:
            raise Http404("شما امکان دسترسی به این صفحه را ندارید")


class AuthorsAccessMixin():
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.is_author or request.user.is_superuser:
                return super().dispatch(request, *args, **kwargs)
            else:
                return redirect('account:profile')
        else:
            return redirect('account:login')
