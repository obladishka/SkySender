from django import forms

from mailings.models import Mailing, Message, Recipient


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


class MailingForm(forms.ModelForm):
    """Форма для добавления или редактирования рассылок."""

    class Meta:
        model = Mailing
        exclude = ("owner", "is_disabled")

    def __init__(self, *args, **kwargs):
        """Метод для стилизации формы."""
        user = kwargs.pop("user")
        super(MailingForm, self).__init__(*args, **kwargs)

        self.fields["start_at"].widget = forms.DateTimeInput(
            attrs={"class": "form-control", "type": "datetime-local", "style": "width: 10em;"}
        )
        self.fields["end_at"].widget = forms.DateTimeInput(
            attrs={"class": "form-control", "type": "datetime-local", "style": "width: 11em;"}
        )
        self.fields["status"].widget.attrs.update(
            {"class": "form-select", "placeholder": "Статус", "style": "width: 5em;"}
        )
        self.fields["message"].queryset = user.messages.all()
        self.fields["message"].widget.attrs.update(
            {"class": "form-select", "placeholder": "Сообщение", "style": "width: 5em;"}
        )
        self.fields["recipients"] = forms.ModelMultipleChoiceField(
            queryset=user.recipients.all(),
        )
        self.fields["recipients"].widget.attrs.update({"style": "width: 15em;"})


class MailingManagerForm(forms.ModelForm):
    """Форма для редактирования товара, доступная для менеджера."""

    class Meta:
        model = Mailing
        fields = ("is_disabled",)

    def __init__(self, *args, **kwargs):
        """Метод для стилизации формы."""
        kwargs.pop("user")
        super(MailingManagerForm, self).__init__(*args, **kwargs)

        self.fields["is_disabled"].widget.attrs.update({"class": "form-check-input"})
        self.fields["is_disabled"].label = "Отключить рассылку"
