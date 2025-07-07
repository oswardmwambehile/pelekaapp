from django.contrib import admin
from .models import Region, District


class DistrictInline(admin.TabularInline):
    model = District
    extra = 0
    readonly_fields = ('created_at', 'updated_at', 'user')
    fields = ('name', 'region', 'user', 'created_at', 'updated_at')
    show_change_link = True


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'created_at', 'updated_at')
    list_filter = ('user',)
    search_fields = ('name', 'user__username')
    readonly_fields = ('created_at', 'updated_at')
    inlines = [DistrictInline]

    def save_model(self, request, obj, form, change):
        if not obj.user:
            obj.user = request.user
        super().save_model(request, obj, form, change)


@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    list_display = ('name', 'region', 'user', 'created_at', 'updated_at')
    list_filter = ('region', 'user')
    search_fields = ('name', 'region__name', 'user__username')
    readonly_fields = ('created_at', 'updated_at')

    def save_model(self, request, obj, form, change):
        if not obj.user:
            obj.user = request.user
        super().save_model(request, obj, form, change)


from django.contrib import admin
from .models import Route

@admin.register(Route)
class RouteAdmin(admin.ModelAdmin):
    list_display = ('origin', 'destination', 'distance', 'expected_time', 'user', 'created_at')
    list_filter = ('user', 'created_at')
    search_fields = ('origin', 'destination', 'user__username')
    readonly_fields = ('created_at', 'updated_at')

    def save_model(self, request, obj, form, change):
        if not obj.pk:  # Only set user on creation
            obj.user = request.user
        super().save_model(request, obj, form, change)
