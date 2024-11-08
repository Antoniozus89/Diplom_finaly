from django.contrib import admin
from django.contrib.admin import AdminSite
from my_blog.models import Post


admin.site.register(Post)


class CustomAdminSite(AdminSite):
    site_header = 'Мой сайт администрирования'
    site_title = 'Админ панель'
    index_title = 'Добро пожаловать на панель управления'


admin_site = CustomAdminSite(name='myadmin')
