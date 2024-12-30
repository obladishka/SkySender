from django.contrib import admin

from mailings.models import Recipient


@admin.register(Recipient)
class RecipientAdmin(admin.ModelAdmin):
    """Класс для кастомной настройки отображения клиентов в админке."""

    list_filter = ("owner",)
