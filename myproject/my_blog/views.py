from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from .forms import PostForm, UserRegistrationForm, CommentForm
from .models import Post


def home(request):
    """Это функция, которая отвечает за отображение домашней страницы приложения."""
    posts = Post.objects.all()
    return render(request, 'blog/home.html', {'posts': posts})


def post_list(request):
    """Эта функция обрабатывает запросы на получение списка всех постов.
    Она извлекает все посты из базы данных с помощью Post.objects.all() и передает их в шаблон post_list.html."""
    post_list = Post.objects.all()
    paginator = Paginator(post_list, 5)  # Показывать 5 постов на странице
    page_number = request.GET.get('page')  # Получаем номер страницы из GET-запроса
    page_obj = paginator.get_page(page_number)  # Получаем объекты для текущей страницы

    return render(request, 'blog/post_list.html', {'page_obj': page_obj})


def post_detail(request, pk):
    """Эта функция обрабатывает запросы на получение подробной информации о конкретном посте.
    Она использует get_object_or_404, чтобы получить пост по первичному ключу (pk). Если пост не найден,
    будет возвращена ошибка 404.
    Пост передается в шаблон post_detail.html.
    'paginator':показывать 5 комментариев на странице"""
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.all()
    paginator = Paginator(comments, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('post_detail', pk=pk)
    else:
        form = CommentForm()

    return render(request, 'blog/post_detail.html', {'post': post, 'form': form, 'page_obj': page_obj})


def add_comment(request, post_id):
    """Это функция, которая добавляет комментарий к посту
    'comment.author':устанавливаем автора комментария
    'return redirect':перенаправление на страницу поста после добавления комментария
    Если GET-запрос или форма не валидна"""
    post = get_object_or_404(Post, pk=post_id)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('post_detail', pk=post_id)


def post_create(request):
    """Эта функция обрабатывает запросы на создание нового поста.Если метод запроса — POST (т.е. форма была отправлена),
    она создает экземпляр формы с данными из запроса и проверяет его на валидность. Если форма валидна,
    данные сохраняются в базе данных, и происходит перенаправление на страницу списка постов.
    Если метод запроса не POST (т.е. пользователь только что открыл страницу), создается пустая форма для ввода данных
    В любом случае форма передается в шаблон post_form.html"""
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'blog/post_form.html', {'form': form})


def post_edit(request, pk):
    """Эта функция обрабатывает запросы на редактирование существующего поста.
    Если метод запроса — POST, создается экземпляр формы с данными из запроса и текущим объектом (instance=post).
    Если форма валидна, изменения сохраняются в базе данных и происходит перенаправление на страницу подробностей
    этого поста."""
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', pk=pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_form.html', {'form': form})


def register(request):
    """Это функция, которая обрабатывает запросы на регистрацию нового пользователя.
    'user.set_password': хранит пароль в зашифрованном виде
    'return redirect': перенаправление на страницу со списком постов  """
    form = UserRegistrationForm()
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')

    return render(request, 'blog/register.html', {'form': form})


def user_login(request):
    """Это функция представления, которая принимает объект request в качестве аргумента. Она обрабатывает запросы
    на вход пользователя.Создается экземпляр формы AuthenticationForm,
    и передаются данные из POST-запроса. Эта форма предназначена для аутентификации пользователей.
    Если метод запроса — POST, это означает, что пользователь отправил форму для входа.
    Функция 'authenticate' проверяет,
    существуют ли указанные имя пользователя и пароль в базе данных. Если аутентификация успешна,
    возвращается объект пользователя; если нет — None. Циклом 'if form.is valid():
    проверяется, является ли форма валидной
    (например, заполнены ли все необходимые поля). Если форма валидна, извлекаются имя пользователя и
    пароль из очищенных данных формы.Функция authenticate проверяет,
    существуют ли указанные имя пользователя и пароль в базе данных. Если аутентификация успешна,
    возвращается объект пользователя; если нет — None. Если пользователь успешно аутентифицирован
    (т.е. user не равен None)
    вызывается функция login, которая устанавливает сессию для пользователя.
    Если метод запроса не POST (т.е. пользователь только что открыл страницу),
    создается пустая форма для ввода данных. В конце функция возвращает
    рендеринг шаблона login.html, передавая в него форму (как контекст)."""
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('post_list')
    else:
        form = AuthenticationForm()

    return render(request, 'blog/login.html', {'form': form})


def success_view(request):
    """Функция представления:
    def success_view(request): — это определение функции представления. Она принимает один аргумент, request,
    который представляет собой объект HTTP-запроса. Этот объект содержит всю информацию о запросе,
    который был отправлен пользователем.
    Отображение шаблона:
    return render(request, 'blog/success.html') — эта строка вызывает функцию render, которая генерирует HTML-ответ
    на основе указанного шаблона.
    request — это объект запроса, который передается в функцию render.
    'blog/success.html' — это путь к шаблону, который будет использоваться для отображения страницы."""
    return render(request, 'blog/success.html')
