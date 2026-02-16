from django.shortcuts import render, redirect, get_object_or_404
from .models import Room

# Home page view
def home(request):
    return render(request, 'booking/home.html')

# Rooms list page view
def rooms_list(request):
    rooms = Room.objects.all()
    return render(request, 'booking/rooms.html', {'rooms': rooms})

# Book a room view
def book_room(request, room_id):
    room = get_object_or_404(Room, id=room_id)

    if room.available:
        room.available = False
        room.save()
        return render(request, 'booking/confirmation.html', {'room': room})
    else:
        # If room is already booked, show error on rooms page
        return render(request, 'booking/rooms.html', {
            'rooms': Room.objects.all(),
            'error': 'This room is already booked!'
        })