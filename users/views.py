import secrets

from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView

from users.forms import UserAuthenticationForm, UserForm
from users.models import User
from users.sevices import UserService


class RegisterView(CreateView):

    model = User
    form_class = UserForm
    template_name = "registration/login.html"
    success_url = reverse_lazy("mailings:main")

    def get_context_data(self, **kwargs):
        """Метод для добавления дополнительных параметров в контекст."""

        context = super().get_context_data(**kwargs)
        context["subject"] = "Спасибо за выбор SkySender!"
        context["text"] = (
            "Для завершения регистрации подтвердите свой Email, перейдя по ссылке, отправленной на Вашу почту."
        )
        return context

    def form_valid(self, form):
        """Метод для кастомизации логики обработки формы."""
        user = form.save()
        user.is_active = False
        user.token = secrets.token_hex(16)
        user.save()

        host = self.request.get_host()
        UserService.send_verification_email(user, host)
        return super().form_valid(form)


class UserLoginView(LoginView):

    model = User
    form_class = UserAuthenticationForm
