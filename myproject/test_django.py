import os
import time
import django

"""Установка переменной окружения для настроек Django"""
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

"""Инициализируйте Django"""
django.setup()

"""Импортируйте модели после инициализации Django"""
from my_blog.models import Post

"""Функция для создания записей"""


def create_posts(num_posts):
    start_time = time.time()
    for i in range(num_posts):
        Post.objects.create(title=f'Post {i}', content='This is a test post.')
    end_time = time.time()
    print(f'Создание {num_posts} записей заняло {end_time - start_time:.2f} секунд.')


"""Функция для выборки всех записей"""
def fetch_posts():
    start_time = time.time()
    posts = Post.objects.all()
    end_time = time.time()
    print(f'Выборка {len(posts)} записей заняла {end_time - start_time:.2f} секунд. ')


"""Функция для удаления всех записей"""


def delete_posts():
    start_time = time.time()
    count = Post.objects.count()
    Post.objects.all().delete()
    end_time = time.time()
    print(f'Удаление {count} записей заняло {end_time - start_time:.2f} секунд.')


"""Запуск программы"""
if __name__ == '__main__':
    num_posts = 1000
    create_posts(num_posts)
    fetch_posts()
    delete_posts()
