from django.contrib import admin
from .models import TrackingStatus

@admin.register(TrackingStatus)
class TrackingStatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'booking', 'status', 'timestamp', 'gps_coordinates')
    search_fields = ('booking__id', 'status')
    list_filter = ('status',)
    list_per_page = 20
