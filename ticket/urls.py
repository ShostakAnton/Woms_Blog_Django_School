from django.urls import path
from . import views


urlpatterns = [
    # path('', views.MyView.as_view()),
    path('add-ticket/', views.AddTicket.as_view())
]

