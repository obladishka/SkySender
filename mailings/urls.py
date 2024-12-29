from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.views.decorators.cache import cache_page

from mailings.apps import MailingsConfig
from mailings.views import MainView

app_name = MailingsConfig.name

urlpatterns = [
    path("", MainView.as_view(), name="main"),
    # path("detail/<int:pk>/", cache_page(60 * 15)(ProductDetailView.as_view()), name="product_detail"),
    # path("new/", ProductCreateView.as_view(), name="add_product"),
    # path("<int:pk>/edit/", ProductUpdateView.as_view(), name="edit_product"),
    # path("<int:pk>/delete/", ProductDeleteView.as_view(), name="delete_product"),
    # path("contacts/", ContactsListViewWithPost.as_view(), name="contacts"),
    # path("category/<int:pk>/", CategoryDetailView.as_view(), name="category_detail"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
