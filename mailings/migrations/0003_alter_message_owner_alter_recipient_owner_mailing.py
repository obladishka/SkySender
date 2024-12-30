# Generated by Django 5.1.4 on 2024-12-30 09:26

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mailings", "0002_message"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name="message",
            name="owner",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="messages",
                to=settings.AUTH_USER_MODEL,
                verbose_name="ответственный",
            ),
        ),
        migrations.AlterField(
            model_name="recipient",
            name="owner",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="recipients",
                to=settings.AUTH_USER_MODEL,
                verbose_name="ответственный",
            ),
        ),
        migrations.CreateModel(
            name="Mailing",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "start_at",
                    models.DateTimeField(
                        blank=True,
                        help_text="Выберите дату и время первой отправки",
                        null=True,
                        verbose_name="дата и время первой отправки",
                    ),
                ),
                (
                    "end_at",
                    models.DateTimeField(
                        blank=True,
                        help_text="Выберите дату и время окончания отправки",
                        null=True,
                        verbose_name="дата и время окончания отправки",
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[("created", "создана"), ("started", "запущена"), ("finished", "завершена")],
                        help_text="Выберите статус рассылки",
                        max_length=8,
                        verbose_name="статус",
                    ),
                ),
                ("is_disabled", models.BooleanField(default=False, verbose_name="отключена")),
                (
                    "message",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, to="mailings.message", verbose_name="сообщение"
                    ),
                ),
                (
                    "owner",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="mailings",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="ответственный",
                    ),
                ),
                ("recipients", models.ManyToManyField(to="mailings.recipient", verbose_name="получатели")),
            ],
            options={
                "verbose_name": "рассылка",
                "verbose_name_plural": "рассылки",
                "permissions": [("can_disable_mailing", "может отключить рассылку")],
            },
        ),
    ]