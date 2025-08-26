from django.urls import path
from . import views

app_name = 'quotes'
urlpatterns = [
    path('', views.random_quote, name='random_quote'),
]