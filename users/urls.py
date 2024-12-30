from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView
from django.urls import path

from users.apps import UsersConfig
from users.sevices import UserService
from users.views import RegisterView, UserLoginView

app_name = UsersConfig.name

urlpatterns = [
    path("login/", UserLoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("register/", RegisterView.as_view(), name="register"),
    path("user-verification/<str:token>", UserService.user_verification, name="user_verification"),
    #     path("account/<int:pk>/", UserDetailView.as_view(), name="user_account"),
    #     path("account/<int:pk>/products", UserProductListView.as_view(), name="user_product_list"),
    #     path("account/<int:pk>/edit", UserUpdateView.as_view(), name="edit_user"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
