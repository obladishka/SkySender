import smtplib

from django.core.mail import send_mail
from django.shortcuts import redirect
from django.urls import reverse

from mailings.models import Attempt, Mailing


class MailingService:
    """Класс для формирования бизнес-логики для работы с рассылками."""

    @staticmethod
    def send_mailing(request, pk):
        """Функция для отправки рассылки через сайт."""

        mailing = Mailing.objects.get(pk=pk)
        subject = mailing.message.subject
        message = mailing.message.message
        recipients = [recipient.email for recipient in mailing.recipients.all()]

        try:
            response = send_mail(subject, message, None, recipients, fail_silently=False)
        except smtplib.SMTPException as e:
            MailingService.log_attempt(status="unsuccessful", response=e, mailing=mailing)
        else:
            MailingService.log_attempt(status="successful", response=response, mailing=mailing)
        finally:
            return redirect(reverse("mailings:mailing_list"))

    @staticmethod
    def log_attempt(status, response, mailing):
        """Функция для создания записи о попытке рассылки."""
        attempt = Attempt.objects.create(status=status, server_response=response, mailing=mailing)
        attempt.save()
