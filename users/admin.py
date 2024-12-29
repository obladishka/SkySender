from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Класс для регистрации модели пользователей в админке."""

    exclude = (
        "password",
        "token",
    )
