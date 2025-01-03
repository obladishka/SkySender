import secrets

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView

from users.forms import UserAuthenticationForm, UserForm, UserManagerForm
from users.models import User
from users.sevices import UserService


class RegisterView(CreateView):

    model = User
    form_class = UserForm
    template_name = "registration/login.html"
    success_url = reverse_lazy("mailings:main")

    def form_valid(self, form):
        """Метод для кастомизации логики обработки формы."""
        user = form.save()
        user.is_active = False
        user.token = secrets.token_hex(16)
        user.save()

        host = self.request.get_host()
        UserService.send_verification_email(user, host)
        return super().form_valid(form)


class UserLoginView(LoginView):

    model = User
    form_class = UserAuthenticationForm


class UserListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    """Класс для отображения списка пользователей."""

    model = User
    permission_required = "users.view_user"
    context_object_name = "users"


class UserUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    """Класс для блокировки пользователей."""

    model = User
    form_class = UserManagerForm
    context_object_name = "user"
    permission_required = "users.can_block_user"
    success_url = reverse_lazy("users:user_list")

    def form_valid(self, form):
        """Метод для кастомизации логики обработки формы."""
        user = form.save()
        if user.is_blocked:
            user.is_active = False
            user.save()
        return super().form_valid(form)
