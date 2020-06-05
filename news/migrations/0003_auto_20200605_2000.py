# Generated by Django 3.0.7 on 2020-06-05 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата добавления'),
        ),
        migrations.AddField(
            model_name='comments',
            name='moderation',
            field=models.BooleanField(default=False),
        ),
    ]