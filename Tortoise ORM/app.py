from tortoise import Tortoise, fields
from tortoise.models import Model

"""Определение модели 'Post'. В которой id: Поле типа IntField, которое является первичным ключом (pk=True). 
Это означает, что это поле будет уникальным для каждой записи.'title': 
Поле типа CharField, которое хранит заголовок поста. max_length=200 указывает максимальную длину заголовка.
'content': Поле типа TextField, которое используется для хранения содержимого поста.
published_date: Поле типа DatetimeField, которое автоматически заполняется текущей датой и временем при 
создании записи (auto_now_add=True)."""


class Post(Model):
    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=200)
    content = fields.TextField()
    published_date = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "posts"


"""Meta: Вложенный класс, который позволяет задавать метаданные для модели. 
В данном случае указывается имя таблицы в базе данных — "posts"."""


class Meta:
    table = "posts"


"""Асинхронная функция 'run'. Tortoise.init(): Эта функция инициализирует соединение с базой данных.
db_url: URL подключения к базе данных PostgreSQL. В данном случае используется пользователь postgres,
 пароль 890227, и база данных называется TortoiseORM.
'modules': Здесь указывается, где находятся мои модели. '__main__' означает, что модели находятся в
текущем модуле (в данном случае в том же файле).
'Tortoise.generate_schemas()': Эта функция генерирует схемы базы данных на основе определенных моделей. 
Если таблицы еще не существуют, они будут созданы.
Добавление записи.'await Post.create' Эта строка создает новую запись в таблице posts с заголовком "Мой первый пост"
и содержимым 'Это содержимое моего первого поста.'."""


async def run():
    await Tortoise.init(
        db_url='postgres://postgres:890227@localhost/TortoiseORM',
        modules={'models': ['__main__']}
    )

    await Tortoise.generate_schemas()

    await Post.create(title='Мой первый пост', content='Это содержимое моего первого поста.')

    await Tortoise.close_connections()


"""Здесь используется модуль asyncio, который позволяет запускать асинхронные функции в Python. 
Функция asyncio.run(run()) запускает асинхронную функцию run"""
import asyncio

asyncio.run(run())
