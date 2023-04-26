from django.contrib import admin
from django.urls import path
from bookings import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.get_bookings, name='get_bookings'),
    path('add/', views.add_booking, name='add_booking'),
    path('available_time_slots/<str:date>/', views.available_time_slots, name='available_time_slots'),
    path('confirm_booking/<int:booking_id>/', views.confirm_booking, name='confirm_booking'),
    path('accounts/', include('accounts.urls')),
]