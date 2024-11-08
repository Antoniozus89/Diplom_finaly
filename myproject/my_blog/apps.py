from django.apps import AppConfig


class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'my_blog'


from django.apps import AppConfig


"""Создается новый класс BlogConfig, который наследует от AppConfig.
Этот класс будет использоваться для конфигурации приложения под названием "blog". Этот параметр указывает,
какой тип поля будет использоваться по умолчанию для автоматического создания первичных ключей в
моделях приложения. В данном случае используется BigAutoField, который позволяет создавать большие
целочисленные идентификаторы (например, для больших таблиц).
'name': Это имя моего приложения. Оно должно совпадать с именем папки моего
приложения (в данном случае — my_blog). Django использует это имя для идентификации приложения в проекте."""
class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'my_blog'


