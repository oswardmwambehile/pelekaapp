from django.contrib import admin
from .models import TransportCompany, Vehicle

@admin.register(TransportCompany)
class TransportCompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'company_name', 'user', 'verified')
    list_filter = ('verified',)
    search_fields = ('company_name', 'user__email')
    list_per_page = 20

@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('id', 'number_plate', 'company', 'vehicle_type', 'capacity', 'is_active')
    list_filter = ('vehicle_type','is_active',)
    search_fields = ('number_plate', 'company__company_name')
    list_per_page = 20
