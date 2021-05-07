from . import views
from django.urls import path

app_name = 'blog'
urlpatterns = [
    path('', views.ArticleList.as_view(), name='home'),
    path('page/<int:page>', views.ArticleList.as_view(), name='home'),
    path('detail/<slug:slug>', views.ArticleDetail.as_view(), name='detail'),
    path('category/<slug:slug>', views.CategoryList.as_view(), name='category'),
    path('category/<slug:slug>/page/<int:page>', views.CategoryList.as_view(), name='category'),
]