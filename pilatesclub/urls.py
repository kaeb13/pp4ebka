"""pilatesclub URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from bookings.views import get_bookings, add_booking, available_time_slots

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', get_bookings, name='get_bookings'),
    path('add/', add_booking, name='add_booking'),
    path('available_time_slots/<str:date>/', available_time_slots, name='available_time_slots'),
 
]
