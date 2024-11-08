import asyncio
from tortoise import Tortoise, fields
from tortoise.models import Model
import time

"""Здесь создается модель Post, представляющая запись в базе данных. Она имеет три поля:
id: Целочисленное поле, которое является первичным ключом.
title: Строковое поле с максимальной длиной 200 символов.
content: Текстовое поле для хранения содержимого поста."""


class Post(Model):
    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=200)
    content = fields.TextField()


"""Инициализация базы данных.
 Асинхронная функция init() инициализирует соединение с базой данных PostgreSQL по 
 указанному URL и генерирует схемы для моделей."""


async def init():
    await Tortoise.init(
        db_url='postgres://postgres:890227@localhost:5432/TortoiseORM',
        modules={'models': ['__main__']}
    )
    await Tortoise.generate_schemas()


"""Создание записей.Функция create_posts(num_posts) создает заданное количество постов. Она:
Измеряет время начала операции.
Создает список постов с помощью генератора списка.
Использует метод 'bulk_create()' для массового добавления постов в базу данных.
Измеряет и выводит время выполнения операции."""


async def create_posts(num_posts):
    start_time = time.time()
    post_list = [Post(title=f'Post {i}', content='This is a test post.') for i in range(num_posts)]
    await Post.bulk_create(post_list)
    end_time = time.time()
    print(f'Создание {num_posts} записей заняло {end_time - start_time:.2f} секунд.')


"""Выборка записей. Функция fetch_posts() извлекает все записи из таблицы Post и выводит время, 
затраченное на выборку, а также общее количество записей. """


async def fetch_posts():
    start_time = time.time()
    posts = await Post.all()
    end_time = time.time()
    print(f'Выборка {num_posts} записей заняла {end_time - start_time:.2f} секунд.')


"""Функция delete_posts() удаляет все записи из таблицы Post и выводит время, затраченное на удаление."""


async def delete_posts():
    start_time = time.time()
    await Post.all().delete()
    end_time = time.time()
    print(f'Удаление {num_posts} записей заняло {end_time - start_time:.2f} секунд.')


"""Функция main(num_posts) выполняет последовательные шаги: инициализация базы данных, 
создание постов, выборка постов и их удаление. В конце она закрывает соединения с базой данных."""


async def main(num_posts):
    await init()
    await create_posts(num_posts)
    await fetch_posts()
    await delete_posts()
    await Tortoise.close_connections()


"""Запуск программы. Если скрипт запускается как основная программа,
 он создает 1000 постов и выполняет все описанные выше операции асинхронно."""
if __name__ == '__main__':
    num_posts = 1000
    asyncio.run(main(num_posts))
