from django.db import models
from .validators import ascii_only_validator


class ChatUser(models.Model):
    username = models.CharField(
        max_length=32, validators=[ascii_only_validator]
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username


class Chat(models.Model):
    chat_id = models.CharField(
        max_length=64, validators=[ascii_only_validator]
    )
    created_at = models.DateTimeField(auto_now_add=True)
    users = models.ManyToManyField(ChatUser, through="Message")

    def __str__(self):
        return self.chat_id


class Message(models.Model):
    text = models.CharField(max_length=256, validators=[ascii_only_validator])
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(ChatUser, on_delete=models.CASCADE)
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)

    def __str__(self):
        return self.text + " - " + self.user.username
