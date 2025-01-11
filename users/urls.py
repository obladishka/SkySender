from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import (LogoutView, PasswordResetCompleteView, PasswordResetConfirmView,
                                       PasswordResetDoneView, PasswordResetView)
from django.urls import path, reverse_lazy

from users.apps import UsersConfig
from users.forms import UserPasswordResetForm, UserSetPasswordForm
from users.sevices import UserService
from users.views import RegisterView, UserListView, UserLoginView, UserUpdateView

app_name = UsersConfig.name

urlpatterns = [
    path("login/", UserLoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("register/", RegisterView.as_view(), name="register"),
    path("user-verification/<str:token>/", UserService.user_verification, name="user_verification"),
    path(
        "password-reset/",
        PasswordResetView.as_view(
            template_name="users/password_reset_form.html",
            form_class=UserPasswordResetForm,
            email_template_name="users/password_reset_email.html",
            success_url=reverse_lazy("users:password_reset_done"),
        ),
        name="password_reset",
    ),
    path(
        "password-reset/done/",
        PasswordResetDoneView.as_view(template_name="users/password_reset_done.html"),
        name="password_reset_done",
    ),
    path(
        "password-reset/<uidb64>/<token>/",
        PasswordResetConfirmView.as_view(
            template_name="users/password_reset_confirm.html",
            form_class=UserSetPasswordForm,
            success_url=reverse_lazy("users:password_reset_complete"),
        ),
        name="password_reset_confirm",
    ),
    path(
        "password-reset/complete/",
        PasswordResetCompleteView.as_view(template_name="users/password_reset_complete.html"),
        name="password_reset_complete",
    ),
    path("users/<int:pk>/edit/", UserUpdateView.as_view(), name="edit_user"),
    path("users/", UserListView.as_view(), name="user_list"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
