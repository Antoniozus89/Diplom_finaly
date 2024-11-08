"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from my_blog.admin import admin_site
from my_blog.views import post_list, post_detail, post_create, post_edit, register, user_login, home, add_comment
from my_blog.views import success_view
from django.urls import path

urlpatterns = [
    path('admin/', admin_site.urls),  # Административный интерфейс Django
    path('', home, name='home'),  # Главная страница
    path('posts/', post_list, name='post_list'),  # Список всех постов.
    path('post/<int:pk>/', post_detail, name='post_detail'),  # Просмотр поста
    path('post/new/', post_create, name='post_create'),  # Создание нового поста.
    path('post/<int:pk>/edit/', post_edit, name='post_edit'),  # Редактирование поста
    path('register/', register, name='register'),  # Регистрация
    path('login/', user_login, name='login'),  # Вход
    path('comments/add/<int:post_id>/', add_comment, name='add_comment'),  # Добавление комментария
    path('success/', success_view, name='success')  # Успех
]
