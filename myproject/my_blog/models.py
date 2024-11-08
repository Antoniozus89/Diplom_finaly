from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    """Модель поста"""
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(
        auto_now_add=True)


def __str__(self):
    """ Этот метод переопределяет стандартное строковое представление объекта. Когда вы
        вызываете str() на объекте или когда Django пытается отобразить объект (например, в админке),
        будет вызван этот метод. Метод возвращает значение self.title, что означает,
        что строковое представление объекта будет равно значению поля title этого объекта."""
    return self.title


class Comment(models.Model):
    """Класс 'Comment' наследуется от 'models.Model', что делает его моделью Django.
    Поле post устанавливает связь смоделью 'Post'. Оно является внешним ключом '(ForeignKey)',
    что означает, что каждый комментарий связан с конкретным постом.
    related_name='comments' позволяет вам обращаться к комментариям поста через атрибут comments. Например,
    вы можете получить все комментарии к посту с помощью post.comments.all().on_delete=models.CASCADE указывает,
    что если пост будет удален, все связанные с ним комментарии также будут удалены.
    'author': Это поле устанавливает связь с моделью User. Оно является внешним ключом (ForeignKey),
    что означает, что каждый комментарий связан с конкретным пользователем."""
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


def __str__(self):
    """Этот метод возвращает строковое представление
    объекта комментария. Он будет использоваться, например, в админке Django для отображения комментариев.
    В данном случае возвращается строка вида "Comment by username on post_title",
     что делает вывод более информативным."""
    return f'Comment by {self.author.username} on {self.post.title}'
