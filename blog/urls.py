from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blog/<int:pk>/', views.blog_detail, name='blog_detail'),
    path('tag/<slug:tag>/', views.tag_filter, name='tag_filter'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('create/', views.blog_create, name='blog_create'),
    path('about/', views.about, name='about'),
]
