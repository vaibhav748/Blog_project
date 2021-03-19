from django.urls import path
from . import views


app_name = 'App_Blog'
urlpatterns = [
    path('', views.BlogList.as_view(), name='blog_list'),
    path('create_blog/', views.CreateBlog.as_view(), name="create_blog"),
    path('blog_details/<slug:slug>', views.blog_details, name="blog_details"),
    path('liked_blog/<pk>', views.liked, name='liked_blog'),
    path('unliked_blog/<pk>', views.unliked, name='unliked_blog'),
]