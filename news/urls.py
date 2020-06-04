from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.news_list, name='list_news'),
    path('single/<int:pk>', views.new_single, name="new_single"),
]
