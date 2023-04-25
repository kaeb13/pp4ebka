from django import forms
from .models import Booking, Instructor, WorkoutType


class BookingForm(forms.ModelForm):
    instructor = forms.ModelChoiceField(queryset=Instructor.objects.all())
    workout_type = forms.ModelChoiceField(queryset=WorkoutType.objects.all())

    class Meta:
        model = Booking
        fields = ['date', 'time', 'instructor', 'workout_type']