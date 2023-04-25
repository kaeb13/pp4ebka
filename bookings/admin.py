from django.contrib import admin
from .models import ToBook, TimeSlot, WorkoutType, Booking, Instructor


# Register your models here.


admin.site.register(ToBook)
admin.site.register(TimeSlot)
admin.site.register(Instructor)
admin.site.register(WorkoutType)
admin.site.register(Booking)