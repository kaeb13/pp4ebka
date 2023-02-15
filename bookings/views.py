from django.shortcuts import render, redirect 
from .models import ToBook
from .forms import BookingForm

# Create your views here.


def get_bookings(request):
    items = ToBook.objects.all()
    context = {
        'items': items
    }
    return render(request, 'bookings/bookings.html', context)


def add_booking(request):
    form = BookingForm()
    if request.method == 'POST':
        date = request.POST.get('date')
        time = request.POST.get('time')
        instructor = request.POST.get('instructor')
        description = request.POST.get('description')
        ToBook.objects.create(date=date, time=time, instructor=instructor, description=description)
        return redirect('get_bookings')
    context = {
        'form': form
    }
    return render(request, 'bookings/add_booking.html', context)
