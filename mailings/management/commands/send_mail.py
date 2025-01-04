from django.core.management import BaseCommand
from django.utils import timezone

from mailings.models import Mailing
from mailings.services import MailingService


class Command(BaseCommand):
    help_text = "Команда отправки рассылки через консоль."

    def handle(self, *args, **options):
        mailings = Mailing.objects.filter(status__in=("started", "created"))
        current_date = timezone.now()

        for mailing in mailings:
            if mailing.status == "created" or (
                mailing.status == "started" and mailing.end_at >= current_date if mailing.end_at else 0
            ):
                MailingService.send_mailing(None, mailing.pk)
