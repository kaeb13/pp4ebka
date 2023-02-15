from django import forms
from .models import ToBook


class BookingForm(forms.ModelForm):
    class Meta:
        model = ToBook
        fields = ['date', 'time', 'instructor', 'description']