from datetime import datetime, timedelta
from django.shortcuts import render, redirect
from .models import ToBook, Instructor, Booking, TimeSlot, WorkoutType
from .forms import BookingForm
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist


def get_bookings(request):
    items = ToBook.objects.all()
    context = {
        'items': items
    }
    return render(request, 'bookings/bookings.html', context)


def add_booking(request):
    instructors_data = [
        {'name': 'Sarah', 'experience': '10 years', 'specialization': 'Mat Pilates'},
        {'name': 'Juan', 'experience': '5 years', 'specialization': 'Barre Pilates'},
        {'name': 'Michael', 'experience': '7 years', 'specialization': 'Power Pilates'},
        {'name': 'Rachel', 'experience': '3 years', 'specialization': 'Reformer Pilates'},
    ]

    for instructor_data in instructors_data:
        try:
            Instructor.objects.get(name=instructor_data['name'])
        except ObjectDoesNotExist:
            instructor = Instructor(
                name=instructor_data['name'],
                experience=instructor_data['experience'],
                specialization=instructor_data['specialization']
            )
            instructor.save()

    instructors = Instructor.objects.all()

    workouts = [
        {'name': 'Mat Pilates', 'description': 'A basic pilates class that focuses on the fundamentals and building core strength'},
        {'name': 'Reformer Pilates', 'description': 'A more advanced class that uses a machine called a reformer to add resistance and intensity to the exercises'},
        {'name': 'Barre Pilates', 'description': 'A hybrid class that combines pilates with ballet-inspired movements at a barre'},
        {'name': 'Power Pilates', 'description': 'A high-energy class that incorporates cardio and strength training into the traditional pilates moves'},
    ]

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('get_bookings')
    else:
        form = BookingForm()

    instructor_id = request.GET.get('instructor')
    workout_type_id = request.GET.get('workout_type')
    date = datetime.now().date()

    if instructor_id and workout_type_id:
        instructor = Instructor.objects.get(id=instructor_id)
        workout_type = WorkoutType.objects.get(id=workout_type_id)

        # Get all bookings for the given date, instructor, and workout type
        bookings = Booking.objects.filter(date=date, instructor=instructor, workout_type=workout_type)

        # Get all time slots for the given date
        time_slots = TimeSlot.objects.filter(date=date)

        # Remove the time slots that are already booked
        booked_time_slots = [booking.time for booking in bookings]
        available_time_slots = [time_slot for time_slot in time_slots if time_slot.time not in booked_time_slots]

        context = {
            'form': form,
            'instructors': instructors,
            'workouts': workouts,
            'time_slots': available_time_slots,
            'current_time': datetime.now(),
        }

    else:
        context = {
            'form': form,
            'instructors': instructors,
            'workouts': workouts,
            'time_slots': [],
            'current_time': datetime.now(),
        }

    return render(request, 'bookings/add_booking.html', context)


def get_time_slots(date, instructor_id, workout_type_id):
    instructor = Instructor.objects.get(id=instructor_id)
    workout_type = WorkoutType.objects.get(id=workout_type_id)

    # Get all bookings for the given date, instructor, and workout type
    bookings = Booking.objects.filter(date=date, instructor=instructor, workout_type=workout_type)

    # Get all time slots for the given date
    time_slots = TimeSlot.objects.filter(date=date)

    # Remove the time slots that are already booked
    booked_time_slots = [booking.time for booking in bookings]
    available_time_slots = [time_slot for time_slot in time_slots if time_slot.time not in booked_time_slots]

    # Return the list of available time slots
    return available_time_slots


def available_time_slots(request, date):
    instructor_id = request.GET.get('instructor')
    workout_type_id = request.GET.get('workout_type')
    
    if instructor_id and workout_type_id:
        time_slots = get_time_slots(date, instructor_id, workout_type_id)
    else:
        time_slots = []
    
    available_slots = [(slot.time.strftime("%H:%M"), slot.id) for slot in time_slots]
    return JsonResponse({'available_slots': available_slots})