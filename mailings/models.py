from django.db import models

from users.models import User


class Recipient(models.Model):
    """Модель получателей рассылки"""

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
        verbose_name="пользователь",
    )

    def __str__(self):
        return f"{self.name}, {self.email}" if self.name else self.email

    class Meta:
        verbose_name = "клиент"
        verbose_name_plural = "клиенты"
