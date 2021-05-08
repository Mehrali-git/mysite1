from . import views
from django.urls import path

app_name = 'blog'
urlpatterns = [
    path('', views.home, name='home'),
    path('detail/<slug:slug>', views.detail, name='detail'),
    path('page/<int:page>', views.home, name='home'),
    path('category/<slug:slug>', views.category, name='category'),
    path('category/<slug:slug>/page/<int:page>', views.category, name='category'),
    path('author/<slug:username>', views.author, name='author'),
    path('author/<slug:username>/page/<int:page>', views.author, name='author'),
]
