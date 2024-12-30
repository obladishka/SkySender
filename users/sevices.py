from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils.html import strip_tags

from users.models import User


class UserService:
    """Класс для формирования бизнес-логики для работы с пользователями."""

    @staticmethod
    def send_verification_email(user, host):
        """Функция для отправки письма для завершения регистрации."""

        context = {
            "url": f"http://{host}/users/user-verification/{user.token}",
        }

        subject = "Добро пожаловать в SkySender!"
        html_message = render_to_string("registration/welcome_letter.html", context)
        plain_message = strip_tags(html_message)

        send_mail(subject, plain_message, None, [user.email], html_message=html_message)

    @staticmethod
    def user_verification(request, token):
        """Функция для подтверждения почты."""
        user = get_object_or_404(User, token=token)
        user.is_active = True
        user.save()
        return redirect(reverse("users:login"))
