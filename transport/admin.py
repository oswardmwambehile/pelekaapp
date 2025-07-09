from django.contrib import admin
from .models import TransportCompany, Vehicle

# Inline for Vehicle's routes ManyToMany
class RouteInline(admin.TabularInline):
    model = Vehicle.routes.through  # The through model for ManyToManyField
    extra = 1
    verbose_name = "Route"
    verbose_name_plural = "Routes"

@admin.register(TransportCompany)
class TransportCompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'company_name', 'user', 'verified')
    list_filter = ('verified',)
    search_fields = ('company_name', 'user__email')
    list_per_page = 20

@admin.action(description='Mark selected vehicles as active')
def make_active(modeladmin, request, queryset):
    queryset.update(is_active=True)

@admin.action(description='Mark selected vehicles as inactive')
def make_inactive(modeladmin, request, queryset):
    queryset.update(is_active=False)

@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('id', 'number_plate', 'company', 'vehicle_type', 'capacity', 'is_active', 'display_routes')
    list_filter = ('vehicle_type', 'is_active',)
    search_fields = ('number_plate', 'company__company_name')
    list_per_page = 20
    inlines = [RouteInline]
    actions = [make_active, make_inactive]
    ordering = ('company__company_name', 'number_plate')

    def display_routes(self, obj):
        routes = obj.routes.all()
        return ", ".join(f"{route.origin} to {route.destination}" for route in routes)
    display_routes.short_description = "Routes"

    # Optional: make number_plate readonly after creation
    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['number_plate']
        return []
