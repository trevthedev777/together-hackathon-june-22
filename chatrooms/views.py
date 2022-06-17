from django.shortcuts import render
from .models import Chatroom

# Create your views here.

def chatrooms(request):
    """
    A view to display all the chatrooms
    """
    chatroom = Chatroom.objects.all()


    template = 'chatrooms/chatrooms.html'
    context = {
        'chatroom': chatroom,
    }

    return render(request, template, context)
