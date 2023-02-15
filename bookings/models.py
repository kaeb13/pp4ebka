from django.db import models

# Create your models here.


class ToBook(models.Model):
    date = models.DateField()
    time = models.TimeField()
    instructor = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField()

    def __str__(self):
        return self.description
