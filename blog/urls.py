from . import views
from django.urls import path
app_name='blog'
urlpatterns = [
    # path('', views.home,name='home'),
    # path('page/<int:page>',views.home,name='home'),
    # path('detail/<slug:slug>',views.detail,name='detail'),
    # path('category/<slug:slug>',views.category,name='category'),
    # path('category/<slug:slug>/page/<int:page>',views.category,name='category'),
    # path('author/<slug:username>',views.author,name='author'),
    # path('author/<slug:username>/page/<int:page>',views.author,name='author'),
    path('', views.ArticleList.as_view(),name='home'),
    path('page/<int:page>',views.ArticleList.as_view(),name='home'),
    path('detail/<slug:slug>',views.ArticleDetail.as_view(),name='detail'),
    path('category/<slug:slug>',views.CategoryList.as_view(),name='category'),
    path('category/<slug:slug>/page/<int:page>',views.CategoryList.as_view(),name='category'),
    path('author/<slug:username>',views.AuthorList.as_view(),name='author'),
    path('author/<slug:username>/page/<int:page>',views.AuthorList.as_view(),name='author'),
]
