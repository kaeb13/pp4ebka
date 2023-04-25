# Generated by Django 3.2.18 on 2023-04-25 08:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0005_timeslot'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkoutType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='booking',
            name='workout',
        ),
        migrations.AddField(
            model_name='booking',
            name='instructor',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='bookings.instructor'),
        ),
        migrations.AddField(
            model_name='booking',
            name='workout_type',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='bookings.workouttype'),
        ),
    ]
