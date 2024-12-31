from django import forms

from mailings.models import Message, Recipient


class RecipientForm(forms.ModelForm):
    """Форма для добавления или редактирования клиентов."""

    class Meta:
        model = Recipient
        exclude = ("owner",)

    def __init__(self, *args, **kwargs):
        """Метод для стилизации формы."""
        super(RecipientForm, self).__init__(*args, **kwargs)
        self.fields["email"].widget.attrs.update(
            {"class": "form-control", "placeholder": "name@example.com", "required": True, "style": "width: 13em;"}
        )
        self.fields["name"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Ф.И.О. клиента", "style": "width: 13em;"}
        )
        self.fields["comment"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Комментарий по клиенту", "style": "height: 5em; width: 25em;"}
        )


class MessageForm(forms.ModelForm):
    """Форма для добавления или редактирования сообщений."""

    class Meta:
        model = Message
        exclude = ("owner",)

    def __init__(self, *args, **kwargs):
        """Метод для стилизации формы."""
        super(MessageForm, self).__init__(*args, **kwargs)
        self.fields["subject"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Тема письма", "required": True, "style": "width: 15em;"}
        )
        self.fields["message"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Текст письма", "style": "height: 5em;"}
        )
