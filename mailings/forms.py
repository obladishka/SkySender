from django import forms

from mailings.models import Recipient


class RecipientForm(forms.ModelForm):
    """Форма для добавления или редактирования клиентов."""

    class Meta:
        model = Recipient
        exclude = ("owner",)

    def __init__(self, *args, **kwargs):
        """Метод для стилизации формы."""
        super(RecipientForm, self).__init__(*args, **kwargs)
        self.fields["email"].widget.attrs.update(
            {"class": "form-control", "placeholder": "name@example.com", "required": True}
        )
        self.fields["name"].widget.attrs.update({"class": "form-control", "placeholder": "Ф.И.О. клиента"})
        self.fields["comment"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Комментарий по клиенту", "style": "height: 1em;"}
        )
