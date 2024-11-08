from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime, func
from sqlalchemy.orm import declarative_base, sessionmaker

"""Создание подключения к базе данных. Где создается объект 'engine',
который устанавливает соединение с базой данных 'PostgreSQL' по указанному URL. 
В данном случае используется пользователь postgres, пароль 890227, и база данных называется SqlAlchemy."""
engine = create_engine('postgresql://postgres:890227@localhost/SqlAlchemy')

"""Определение базового класса. Base — это базовый класс для всех моделей SQLAlchemy. 
Все мои модели должны наследовать от этого класса."""
Base = declarative_base()

"""Определение модели Post.Где tablename: Указывает имя таблицы в базе данных — в данном случае это 'posts'.
id: Поле типа Integer, которое является первичным ключом (primary_key=True).
title: Поле типа String, максимальная длина которого составляет 200 символов. Оно не может быть пустым (nullable=False).
content: Поле типа Text, которое также не может быть пустым.
published_date: Поле типа DateTime,
которое автоматически заполняется текущей датой и временем при создании записи (server_default=func.now())."""


class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False)
    content = Column(Text, nullable=False)
    published_date = Column(DateTime, server_default=func.now())


"""Создание таблиц в базе данных. Эта строка создает все таблицы в базе данных на основе определенных моделей. 
   Если таблицы уже существуют, они не будут перезаписаны."""
Base.metadata.create_all(engine)

"""Создание сессии. 
'sessionmaker': Создает класс сессии, который будет использоваться для взаимодействия с базой данных.
Создается экземпляр сессии session, который будет использоваться для выполнения операций с базой данных."""
Session = sessionmaker(bind=engine)
session = Session()

"""Добавление новой записи.
В блоке 'try' создается новый объект 'Post' с заголовком и содержимым.
Метод 'session.add(new_post)' добавляет новый объект в текущую сессию.
Метод 'session.commit()' сохраняет изменения в базе данных.
Если операция прошла успешно, выводится сообщение "Новое соообщение успешно добавлено!".
Если возникает ошибка (например, проблемы с подключением к базе данных), она будет поймана в блоке 'except', 
и выведется сообщение об ошибке.
В блоке 'finally' вызывается метод 'session.close()', чтобы закрыть сессию и освободить ресурсы."""
try:

    new_post = Post(title='Мой первый пост.', content='Это содержание моего первого поста.')
    session.add(new_post)
    session.commit()
    print("Новый пост успешно добавлен!")
except Exception as e:
    print(f"Произошла ошибка: {e}")
finally:
    session.close()
