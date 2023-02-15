from django.shortcuts import render
from .models import ToBook

# Create your views here.


def get_bookings(request):
    items = ToBook.objects.all()
    context = {
        'items': items
    }
    return render(request, 'bookings/bookings.html', context)


def add_booking(request):
    return render(request, 'bookings/add_booking.html')    
