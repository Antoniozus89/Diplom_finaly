from django import forms
from django.contrib.auth.models import User
from .models import Post, Comment


class UserRegistrationForm(forms.ModelForm):
    """class UserRegistrationForm(forms.ModelForm): — определяет класс формы, наследующий от ModelForm.
    Это позволяет автоматически создавать форму на основе модели User.
    Поля формы:
    password и password_confirm — определены как поля типа CharField, но с использованием виджета PasswordInput,
    что скрывает вводимые символы (для безопасности).
    Обратите внимание, что поле password_confirm не указано в классе Meta,
    поскольку оно используется только для валидации.
    Класс Meta:
    Внутренний класс Meta указывает, что форма связана с моделью User и определяет поля,
    которые будут включены в форму (username, email, и password).
    Метод валидации:
    Метод clean(self) переопределяет стандартный метод валидации формы.
    Он выполняет дополнительную проверку на совпадение паролей.
    Если пароли не совпадают, вызывается исключение forms.ValidationError,
    и пользователю будет показано сообщение об ошибке.
    Метод сохранения:
    Метод save(self, commit=True) переопределяет стандартный метод сохранения формы.
    Он создает объект пользователя, устанавливает его пароль (с помощью метода set_password,
    который хеширует пароль) и сохраняет его в базе данных, если параметр commit установлен в True."""
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError("Пароли не совпадают.")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class PostForm(forms.ModelForm):
    """Этот класс также наследует от ModelForm, что позволяет создавать форму на основе модели Post.
        Meta-класс:
        Указывает, что эта форма связана с моделью Post и определяет поля, которые будут включены в форму:
        title и content. Это означает, что пользователь сможет вводить заголовок и содержимое поста через эту форму."""

    class Meta:
        model = Post
        fields = ['title', 'content']


class CommentForm(forms.ModelForm):
    """Наследование от forms.ModelForm: Как и предыдущие классы, этот класс наследует от ModelForm,
    позволяя создавать форму на основе модели Comment.
    Meta-класс:
    Указывает, что эта форма связана с моделью Comment и определяет поле, которое будет включено в форму:
    только поле content. Это означает, что пользователь сможет вводить текст комментария через эту форму."""

    class Meta:
        model = Comment
        fields = ['content']
