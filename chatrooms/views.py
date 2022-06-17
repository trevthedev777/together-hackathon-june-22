from django.shortcuts import render

# Create your views here.

def chatrooms(request):
    """
    A view to display all the chatrooms
    """
    template = 'chatrooms/chatrooms.html'
    context = {
        # 'chatroom': chatroom,
    }

    return render(request, template)
