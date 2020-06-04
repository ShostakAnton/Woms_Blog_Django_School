from django.contrib import admin
from .models import News, Tag, Category

admin.site.register(News)
admin.site.register(Tag)
admin.site.register(Category)

# Register your models here.
