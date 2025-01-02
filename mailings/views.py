from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, TemplateView, UpdateView

from mailings.forms import MailingForm, MailingManagerForm, MessageForm, RecipientForm
from mailings.models import Mailing, Message, Recipient


class MainView(TemplateView):
    """Класс для отображения главной страницы."""

    template_name = "mailings/main.html"


class RecipientListView(LoginRequiredMixin, ListView):
    """Класс для отображения списка клиентов."""

    model = Recipient
    context_object_name = "recipients"

    def get_queryset(self):
        """Метод для формирования списка клиентов в зависимости от статуса пользователя."""
        user = self.request.user

        if user.has_perm("mailings.can_disable_mailing"):
            return self.model.objects.all()
        return user.recipients.all()


class RecipientDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    """Класс для отображения подробной информации о клиенте."""

    model = Recipient
    permission_required = "mailings.view_recipient"
    context_object_name = "recipient"


class RecipientCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    """Класс для добавления нового клиента."""

    model = Recipient
    form_class = RecipientForm
    success_url = reverse_lazy("mailings:recipient_list")
    permission_required = "mailings.add_recipient"
    template_name = "mailings/recipient_list.html"

    def form_valid(self, form):
        """Метод для кастомизации логики обработки формы."""
        recipient = form.save(commit=False)
        recipient.owner = self.request.user
        recipient.save()
        return super().form_valid(form)


class RecipientUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    """Класс для редактирования информации о клиенте."""

    model = Recipient
    form_class = RecipientForm
    success_url = reverse_lazy("mailings:recipient_list")
    permission_required = "mailings.change_recipient"
    template_name = "mailings/recipient_list.html"


class RecipientDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    """Класс для удаления клиента."""

    model = Recipient
    success_url = reverse_lazy("mailings:recipient_list")
    permission_required = "mailings.delete_recipient"


class MessageListView(LoginRequiredMixin, ListView):
    """Класс для отображения списка сообщений."""

    model = Message
    context_object_name = "messages"

    def get_queryset(self):
        """Метод для формирования списка сообщений текущего пользователя."""

        return self.request.user.messages.all()


class MessageDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    """Класс для отображения полного текста письма."""

    model = Message
    permission_required = "mailings.view_message"
    context_object_name = "message"


class MessageCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    """Класс для добавления нового сообщения."""

    model = Message
    form_class = MessageForm
    success_url = reverse_lazy("mailings:message_list")
    permission_required = "mailings.add_message"
    template_name = "mailings/message_list.html"

    def form_valid(self, form):
        """Метод для кастомизации логики обработки формы."""
        message = form.save(commit=False)
        message.owner = self.request.user
        message.save()
        return super().form_valid(form)


class MessageUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    """Класс для редактирования сообщения."""

    model = Message
    form_class = MessageForm
    success_url = reverse_lazy("mailings:message_list")
    permission_required = "mailings.change_message"
    template_name = "mailings/message_list.html"


class MessageDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    """Класс для удаления сообщения."""

    model = Message
    success_url = reverse_lazy("mailings:message_list")
    permission_required = "mailings.delete_message"


class MailingListView(LoginRequiredMixin, ListView):
    """Класс для отображения списка рассылок."""

    model = Mailing
    context_object_name = "mailings"

    def get_queryset(self):
        """Метод для формирования списка рассылок в зависимости от статуса пользователя."""
        user = self.request.user

        if user.has_perm("mailings.can_disable_mailing"):
            return self.model.objects.all()
        return self.model.objects.filter(owner=user, is_disabled=False)


class MailingDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    """Класс для отображения полной информации о рассылке."""

    model = Mailing
    permission_required = "mailings.view_mailing"
    context_object_name = "mailing"


class MailingCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    """Класс для добавления новой рассылки."""

    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy("mailings:mailing_list")
    permission_required = "mailings.add_mailing"
    template_name = "mailings/mailing_list.html"

    def get_form_kwargs(self):
        """Метод для фильтрации данных в полях формы."""
        kwargs = super().get_form_kwargs()
        kwargs.update({"user": self.request.user})
        return kwargs

    def form_valid(self, form):
        """Метод для кастомизации логики обработки формы."""
        mailing = form.save(commit=False)
        mailing.owner = self.request.user
        mailing.save()
        return super().form_valid(form)


class MailingUpdateView(LoginRequiredMixin, UpdateView):
    """Класс для редактирования рассылки."""

    model = Mailing
    success_url = reverse_lazy("mailings:mailing_list")
    template_name = "mailings/mailing_list.html"

    def get_form_class(self):
        """Метод для выбора формы в зависимости от прав пользователя."""
        user = self.request.user

        if user == self.object.owner:
            return MailingForm
        if user.has_perm("mailings.can_disable_mailing"):
            return MailingManagerForm
        raise PermissionDenied

    def get_form_kwargs(self):
        """Метод для фильтрации данных в полях формы."""
        kwargs = super().get_form_kwargs()
        kwargs.update({"user": self.request.user})
        return kwargs

    def get_template_names(self):
        """Метод для выбора темплейта для формы в зависимости от прав пользователя."""
        user = self.request.user

        if user.has_perm("mailings.can_disable_mailing"):
            return "mailings/mailing_detail.html"
        return "mailings/mailing_list.html"


class MailingDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    """Класс для удаления рассылки."""

    model = Mailing
    success_url = reverse_lazy("mailings:mailing_list")
    permission_required = "mailings.delete_mailing"
