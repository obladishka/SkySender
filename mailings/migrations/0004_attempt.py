# Generated by Django 5.1.4 on 2024-12-30 09:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mailings", "0003_alter_message_owner_alter_recipient_owner_mailing"),
    ]

    operations = [
        migrations.CreateModel(
            name="Attempt",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now_add=True, verbose_name="дата и время попытки")),
                (
                    "status",
                    models.CharField(
                        choices=[("successful", "yспешно"), ("unsuccessful", "не yспешно")],
                        max_length=12,
                        verbose_name="статус",
                    ),
                ),
                ("server_response", models.TextField(verbose_name="ответ почтового сервера")),
                (
                    "mailing",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="mailings.mailing", verbose_name="рассылка"
                    ),
                ),
            ],
            options={
                "verbose_name": "попытка рассылки",
                "verbose_name_plural": "попытки рассылки",
            },
        ),
    ]
