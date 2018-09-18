

from django.urls import path
from . import views

app_name= 'home'
urlpatterns = [
    path('', views.PublicCommentView, name = 'home_page'),
]
