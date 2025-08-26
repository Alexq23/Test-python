from django.contrib import admin
from django.urls import path, include
from quotes import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.random_quote, name='random_quote'),
    path('add/', views.add_quote, name='add_quote'),
    path('top/', views.top_quotes, name='top_quotes'),
    path('like/', views.like_quote, name='like_quote'),
    path('dislike/', views.dislike_quote, name='dislike_quote'),
]