from django.db import models

from config.settings import ATTEMPT_STATUSES, MAILING_STATUSES
from users.models import User


class Recipient(models.Model):
    """Модель получателей рассылки."""

    email = models.EmailField(unique=True, verbose_name="email", help_text="Введите email клиента")
    name = models.CharField(
        max_length=150, verbose_name="Ф.И.О.", help_text="Введите Ф.И.О. клиента", null=True, blank=True
    )
    comment = models.TextField(
        verbose_name="комментарий", help_text="Добавьте комментарий по клиенту", null=True, blank=True
    )
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="recipients",
        verbose_name="ответственный",
    )

    def __str__(self):
        return f"{self.name}, {self.email}" if self.name else self.email

    class Meta:
        verbose_name = "клиент"
        verbose_name_plural = "клиенты"


class Message(models.Model):
    """Модель сообщений."""

    subject = models.CharField(max_length=150, verbose_name="тема письма", help_text="Введите тему письма")
    message = models.TextField(verbose_name="текст письма", help_text="Введите текст письма")
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="messages",
        verbose_name="ответственный",
    )

    def __str__(self):
        return f"{self.subject}: {self.message[:50]}"

    class Meta:
        verbose_name = "сообщение"
        verbose_name_plural = "сообщения"


class Mailing(models.Model):
    """Модель рассылок."""

    start_at = models.DateTimeField(
        verbose_name="дата и время первой отправки",
        help_text="Выберите дату и время первой отправки",
        null=True,
        blank=True,
    )
    end_at = models.DateTimeField(
        verbose_name="дата и время окончания отправки",
        help_text="Выберите дату и время окончания отправки",
        null=True,
        blank=True,
    )
    status = models.CharField(
        max_length=8, choices=MAILING_STATUSES, verbose_name="статус", help_text="Выберите статус рассылки"
    )
    message = models.ForeignKey(Message, on_delete=models.PROTECT, verbose_name="сообщение")
    recipients = models.ManyToManyField(Recipient, verbose_name="получатели")
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="mailings",
        verbose_name="ответственный",
    )
    is_disabled = models.BooleanField(default=False, verbose_name="отключена")

    def __str__(self):
        return f"{self.start_at}-{self.start_at} {self.message}"

    class Meta:
        verbose_name = "рассылка"
        verbose_name_plural = "рассылки"
        permissions = [
            ("can_disable_mailing", "может отключить рассылку"),
        ]


class Attempt(models.Model):
    """Модель попыток рассылок."""

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="дата и время попытки")
    status = models.CharField(max_length=12, choices=ATTEMPT_STATUSES, verbose_name="статус")
    server_response = models.TextField(verbose_name="ответ почтового сервера")
    mailing = models.ForeignKey(Mailing, on_delete=models.CASCADE, verbose_name="рассылка")

    def __str__(self):
        return f"{self.mailing}: {self.status}"

    class Meta:
        verbose_name = "попытка рассылки"
        verbose_name_plural = "попытки рассылки"
