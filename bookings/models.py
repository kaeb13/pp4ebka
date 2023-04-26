from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class ToBook(models.Model):
    date = models.DateField()
    time = models.TimeField()
    instructor = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField()

    def __str__(self):
        return self.description


class Instructor(models.Model):
    name = models.CharField(max_length=50)
    experience = models.CharField(max_length=50, default='No experience listed')
    specialization = models.CharField(max_length=50, default='No specialization listed')

    def __str__(self):
        return self.name


class WorkoutType(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Booking(models.Model):
    date = models.DateField()
    time = models.TimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE, default=None)
    workout_type = models.ForeignKey(WorkoutType, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return f'{self.user.username} - {self.workout_type} - {self.date} - {self.time}'


class TimeSlot(models.Model):
    date = models.DateField()
    time = models.TimeField()
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.time} - {self.date} - {self.instructor}"