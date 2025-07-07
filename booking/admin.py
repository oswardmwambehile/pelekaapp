from django.contrib import admin
from .models import Schedule, Booking

@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('id', 'vehicle', 'route', 'departure_time')
    search_fields = ('vehicle__number_plate', 'route__origin__name', 'route__destination__name')
    list_filter = ('departure_time',)
    list_per_page = 20

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'vehicle', 'parcel', 'date', 'status')
    search_fields = ('vehicle__number_plate', 'parcel__name')
    list_filter = ('status',)
    list_per_page = 20
