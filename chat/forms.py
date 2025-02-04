from django import forms
from .validators import ascii_only_validator


class ChatForm(forms.Form):
    username = forms.CharField(
        max_length=32,
        validators=[ascii_only_validator],
        widget=forms.TextInput(
            attrs={
                "placeholder": "Enter your username",
                "class": "form-control"
            }
        ),
    )
    chat_id = forms.CharField(
        max_length=64,
        validators=[ascii_only_validator],
        widget=forms.TextInput(
            attrs={"placeholder": "Enter chat ID", "class": "form-control"}
        ),
    )
