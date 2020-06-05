from django.contrib import admin
from .models import News, Tag, Category, Comments
import django_summernote.admin


class NewAdmin(django_summernote.admin.SummernoteModelAdmin):
    summernote_fields = ('text_min', 'text',)


admin.site.register(News, NewAdmin)
admin.site.register(Tag)
admin.site.register(Category)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'new', 'created', 'moderation')


admin.site.register(Comments, CommentAdmin)

# Register your models here.
