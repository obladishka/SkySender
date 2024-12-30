from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, TemplateView

from mailings.forms import RecipientForm
from mailings.models import Recipient


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
            return Recipient.objects.all()
        return user.recipients.all()


class RecipientDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    """Класс для отображения подробной информации о клиенте."""

    model = Recipient
    permission_required = "mailings.view_recipient"


class RecipientCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    """Класс для отображения подробной информации о клиенте."""

    form_class = RecipientForm
    success_url = reverse_lazy("mailings:recipient_list")
    permission_required = "mailings.add_recipient"

    def form_valid(self, form):
        """Метод для кастомизации логики обработки формы."""
        recipient = form.save()
        recipient.owner = self.request.user
        recipient.save()
        return super().form_valid(form)
