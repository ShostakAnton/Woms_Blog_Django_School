from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.news_list, name='list_news'),
    path('summernote/', include('django_summernote.urls')),
    path('accounts/', include('allauth.urls')),
    path('single/<int:pk>', views.new_single, name="new_single"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
