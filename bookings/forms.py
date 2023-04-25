from django import forms
from .models import Booking, Instructor


class BookingForm(forms.ModelForm):
    instructor = forms.ModelChoiceField(queryset=Instructor.objects.all())
    workout_type = forms.ChoiceField(choices=(
        ('mat_pilates', 'Mat Pilates'),
        ('reformer_pilates', 'Reformer Pilates'),
        ('barre_pilates', 'Barre Pilates'),
        ('power_pilates', 'Power Pilates'),
    ))

    class Meta:
        model = Booking
        fields = ['date', 'time', 'instructor', 'workout_type']