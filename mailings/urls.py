from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.views.decorators.cache import cache_page

from mailings.apps import MailingsConfig
from mailings.views import MainView, RecipientCreateView, RecipientDetailView, RecipientListView, RecipientUpdateView

app_name = MailingsConfig.name

urlpatterns = [
    path("", MainView.as_view(), name="main"),
    path("recipients/", RecipientListView.as_view(), name="recipient_list"),
    path("recipients/new", RecipientCreateView.as_view(), name="add_recipient"),
    path("recipients/<int:pk>/edit/", RecipientUpdateView.as_view(), name="edit_recipient"),
    path("recipients/<int:pk>/", RecipientDetailView.as_view(), name="recipient_detail"),
    # path("detail/<int:pk>/", cache_page(60 * 15)(ProductDetailView.as_view()), name="product_detail"),
    # path("new/", ProductCreateView.as_view(), name="add_product"),
    # path("<int:pk>/edit/", ProductUpdateView.as_view(), name="edit_product"),
    # path("<int:pk>/delete/", ProductDeleteView.as_view(), name="delete_product"),
    # path("contacts/", ContactsListViewWithPost.as_view(), name="contacts"),
    # path("category/<int:pk>/", CategoryDetailView.as_view(), name="category_detail"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
