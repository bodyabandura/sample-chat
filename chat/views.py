from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Chat, Message
from .forms import ChatForm


def chat_connect(request):
    if request.method == "POST":
        form = ChatForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            chat_id = form.cleaned_data["chat_id"]

            request.session["username"] = username

            chat = Chat.objects.filter(chat_id=chat_id).first()
            if not chat:
                chat = Chat.objects.create(chat_id=chat_id)
            return redirect("chat:chat_room", chat_id=chat_id)
        else:
            messages.error(
                request,
                "Invalid characters in the username or chat ID. "
                "Only ASCII characters are allowed.",
            )
    else:
        form = ChatForm()

    return render(request, "chat/chat_connect.html", {"form": form})


def chat_room(request, chat_id):
    username = request.session.get("username", "Anonymous")

    chat = Chat.objects.get(chat_id=chat_id)
    messages = Message.objects.filter(chat=chat).order_by("created_at")

    return render(
        request,
        "chat/chat_room.html",
        {
            "chat_id": chat_id,
            "username": username,
            "messages": messages,
        },
    )
