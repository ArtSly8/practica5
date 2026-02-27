from django import forms
from django.core.exceptions import ValidationError

class NameForm(forms.Form):
    name = forms.CharField(
        label="Ваше имя",
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            "placeholder": "Введите имя",
            "autocomplete": "name",
        }),
    )

    def clean_name(self):
        value = (self.cleaned_data.get("name") or "").strip()
        if not value:
            raise ValidationError("Поле имени не может быть пустым.")
        return value
