from django.shortcuts import render

# Create your views here.


def get_booking(request):
    return render(request, 'bookings/bookings.html')
