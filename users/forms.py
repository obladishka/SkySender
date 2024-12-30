from django.contrib.auth.forms import AuthenticationForm, UserChangeForm, UserCreationForm

from users.models import User


class UserForm(UserCreationForm):
    """Форма для регистрации новых пользователей."""

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("email", "password1", "password2")

    def __init__(self, *args, **kwargs):
        """Метод для стилизации формы."""
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields["email"].widget.attrs.update(
            {"class": "form-control", "placeholder": "name@example.com", "required": True}
        )
        self.fields["email"].help_text = ""
        self.fields["password1"].label = "Пароль"
        self.fields["password1"].help_text = (
            "Пароль должен содержать не менее 8 символов, состоять не только из цифр и отличаться от почты"
        )
        self.fields["password2"].label = "Подтверждение пароля"
        self.fields["password2"].help_text = ""
        self.fields["password1"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Пароль", "required": True}
        )
        self.fields["password2"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Повторите пароль", "required": True}
        )


class UserAuthenticationForm(AuthenticationForm):
    """Форма для авторизации пользователей."""

    class Meta:
        model = User
        fields = ("email", "password")

    def __init__(self, *args, **kwargs):
        """Метод для стилизации формы."""
        super(UserAuthenticationForm, self).__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update(
            {"class": "form-control", "placeholder": "name@example.com", "required": True}
        )
        self.fields["password"].widget.attrs.update({"class": "form-control", "required": True})
