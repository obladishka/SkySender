from django.core.management import BaseCommand, call_command

from users.models import User


class Command(BaseCommand):
    help = "Добавляет тестовых пользователей в бд, предварительно ее очистив."

    def handle(self, *args, **kwargs):
        User.objects.all().delete()

        call_command("loaddata", "groups_fixture.json", format="json")
        self.stdout.write(self.style.SUCCESS("Добавление пользователей прошло успешно."))
