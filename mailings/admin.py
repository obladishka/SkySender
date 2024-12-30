from django.contrib import admin

from mailings.models import Mailing, Message, Recipient


@admin.register(Recipient)
class RecipientAdmin(admin.ModelAdmin):
    """Класс для кастомной настройки отображения клиентов в админке."""

    list_display = ("email", "name", "comment", "owner")
    list_filter = ("owner",)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    """Класс для кастомной настройки отображения сообщений в админке."""

    list_filter = ("owner",)


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    """Класс для кастомной настройки отображения рассылок в админке."""

    list_filter = ("owner", "is_disabled")
