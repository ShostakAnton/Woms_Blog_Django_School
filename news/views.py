from django.shortcuts import render, get_object_or_404, redirect
from .models import News, Comments
from .forms import CommentForm


def news_list(request):
    """Вывод всех новостей
    """
    news = News.objects.all()
    return render(request, "news/news_list.html", {"news": news})


def new_single(request, pk):
    new = get_object_or_404(News, id=pk)
    comment = Comments.objects.filter(new=pk, moderation=True)
    if request.method == 'POST':    # если POST запрос мы отправляем заполненую форму
        form = CommentForm(request.POST)    # пользователь уже ввел комментарий
        if form.is_valid():     # проверка на коректность
            form = form.save(commit=False)     # приостановление сохранение формы
            form.user = request.user    # присваеваем пользователя который сейчас на сайте
            form.new = new      # присваиваем комментарий текущей статье
            form.save()     # сохранение формы
            return redirect('new_single', pk)   # перенаправление на текущею страницу
    else:                     # если у нас GET запрос мы отображаем пустую форму
        form = CommentForm()
    return render(request, "news/new_single.html",
                  {"new": new,
                   'comments': comment,
                   'form': form, })
