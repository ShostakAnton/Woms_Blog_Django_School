from django.shortcuts import render, get_object_or_404, redirect
from .models import News, Comments
from .forms import CommentForm
from datetime import datetime, timedelta
from django.utils import timezone


def news_list(request):
    """Вывод всех новостей
    """
    news = News.objects.all()
    return render(request, "news/news_list.html", {"news": news})


def new_single(request, pk):
    new = get_object_or_404(News, id=pk)
    comment = Comments.objects.filter(new=pk, moderation=True)
    if request.method == 'POST':  # если POST запрос мы отправляем заполненую форму
        form = CommentForm(request.POST)  # пользователь уже ввел комментарий
        if form.is_valid():  # проверка на коректность
            form = form.save(commit=False)  # приостановление сохранение формы
            form.user = request.user  # присваеваем пользователя который сейчас на сайте
            form.new = new  # присваиваем комментарий текущей статье
            form.save()  # сохранение формы
            return redirect('new_single', pk)  # перенаправление на текущею страницу
    else:  # если у нас GET запрос мы отображаем пустую форму
        form = CommentForm()
    return render(request, "news/new_single.html",
                  {"new": new,
                   'comments': comment,
                   'form': form, })


def news_filter(request, pk):
    """фильтр новостей
    """
    news = News.objects.all()  # выбираем все наши статьи

    if pk == 1:
        now = datetime.now() - timedelta(minutes=60 * 24 * 7)  # текущая дата минус неделя
        news = news.filter(created__gte=now)    # сравниваем больше или равно текущей дате
    elif pk == 2:
        now = datetime.now() - timedelta(minutes=60 * 24 * 30)  # текущая дата минус месяц
        news = news.filter(created__gte=now)
    elif pk == 2:
        news = news

    return render(request, "news/news_list.html", {"news": news})
