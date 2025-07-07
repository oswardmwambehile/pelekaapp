# users/admin.py

from django.contrib import admin
from django.utils.html import format_html
from .models import CustomUser
from django.contrib import admin

admin.site.site_header = "Peleka App Admin"
admin.site.site_title = "Peleka Admin"
admin.site.index_title = "Welcome to Peleka Admin Dashboard"



@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'avatar_thumb', 'email', 'username', 'user_type', 'phone_number', 'is_staff', 'is_active')
    list_filter = ('user_type', 'is_staff', 'is_active')
    search_fields = ('email', 'username', 'phone_number')
    ordering = ('-id',)
    list_per_page = 20  # pagination
    
    fieldsets = (
        ('Basic Info', {'fields': ('email', 'username', 'password')}),
        ('Personal',    {'fields': ('phone_number', 'profile_picture', 'user_type')}),
        ('Permissions', {'fields': ('is_active','is_staff','is_superuser','groups','user_permissions')}),
    )

    readonly_fields = ('avatar_thumb',)

    def avatar_thumb(self, obj):
        if obj.profile_picture:
            return format_html(
                '<img src="{}" style="width:50px; height:50px; border-radius:25px;" />',
                obj.profile_picture.url
            )
        return 'No Image'
    avatar_thumb.short_description = 'Profile Image'

    def get_queryset(self, request):
        return super().get_queryset(request).select_related()
