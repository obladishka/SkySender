from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.views.decorators.cache import cache_page

from mailings.apps import MailingsConfig
from mailings.views import (MailingCreateView, MailingDeleteView, MailingDetailView, MailingListView,
                            MailingUpdateView, MainView, MessageCreateView, MessageDeleteView, MessageDetailView,
                            MessageListView, MessageUpdateView, RecipientCreateView, RecipientDeleteView,
                            RecipientDetailView, RecipientListView, RecipientUpdateView)

app_name = MailingsConfig.name

urlpatterns = [
    path("", MainView.as_view(), name="main"),
    path("recipients/", RecipientListView.as_view(), name="recipient_list"),
    path("recipients/new", RecipientCreateView.as_view(), name="add_recipient"),
    path("recipients/<int:pk>/edit/", RecipientUpdateView.as_view(), name="edit_recipient"),
    path("recipients/<int:pk>/", RecipientDetailView.as_view(), name="recipient_detail"),
    path("recipients/<int:pk>/delete/", RecipientDeleteView.as_view(), name="delete_recipient"),
    path("messages/", MessageListView.as_view(), name="message_list"),
    path("messages/new", MessageCreateView.as_view(), name="add_message"),
    path("messages/<int:pk>/edit/", MessageUpdateView.as_view(), name="edit_message"),
    path("messages/<int:pk>/", MessageDetailView.as_view(), name="message_detail"),
    path("messages/<int:pk>/delete/", MessageDeleteView.as_view(), name="delete_message"),
    path("mailings/", MailingListView.as_view(), name="mailing_list"),
    path("mailings/new", MailingCreateView.as_view(), name="add_mailing"),
    path("mailings/<int:pk>/edit/", MailingUpdateView.as_view(), name="edit_mailing"),
    path("mailings/<int:pk>/", MailingDetailView.as_view(), name="mailing_detail"),
    path("mailings/<int:pk>/delete/", MailingDeleteView.as_view(), name="delete_mailing"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
