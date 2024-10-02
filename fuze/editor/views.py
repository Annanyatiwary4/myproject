from django.shortcuts import render, redirect
from .models import Room, Message
import random
import string

# Helper function to generate random room ID
def generate_room_id():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

# View for creating a new room
def CreateRoomView(request):
    if request.method == "POST":
        username = request.POST["username"]
        room_id = generate_room_id()

        # Create a new room with random room_id
        Room.objects.create(room_id=room_id)

        # Redirect to the created room
        return redirect("room", room_id=room_id, username=username)

    return render(request, "editor.html")

# View for joining an existing room
def JoinRoomView(request):
    if request.method == "POST":
        username = request.POST["username"]
        room_id = request.POST["room_id"]

        try:
            existing_room = Room.objects.get(room_id=room_id)
        except Room.DoesNotExist:
            return redirect('home')  # Handle room not found

        # Redirect to the existing room
        return redirect("room", room_id=room_id, username=username)

    return render(request, "editor.html")

def RoomView(request, room_id, username):
    room = Room.objects.get(room_id=room_id)
    messages = Message.objects.filter(room=room)

    context = {
        'room_name': room_id,
        'user': username,
        'messages': messages,
    }

    return render(request, 'room.html', context)
