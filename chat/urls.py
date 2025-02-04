from django.urls import path
from .views import chat_connect, chat_room


urlpatterns = [
    path("chat/", chat_connect, name="chat_connect"),
    path("chat/<str:chat_id>/", chat_room, name="chat_room"),
]

app_name = "chat"
