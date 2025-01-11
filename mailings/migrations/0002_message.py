# Generated by Django 5.1.4 on 2024-12-30 08:48

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mailings", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Message",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "subject",
                    models.CharField(help_text="Введите тему письма", max_length=150, verbose_name="тема письма"),
                ),
                ("message", models.TextField(help_text="Введите текст письма", verbose_name="текст письма")),
                (
                    "owner",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="messages",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="пользователь",
                    ),
                ),
            ],
            options={
                "verbose_name": "сообщение",
                "verbose_name_plural": "сообщения",
            },
        ),
    ]
