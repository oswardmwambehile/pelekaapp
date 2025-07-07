from django.contrib import admin
from .models import Parcel

@admin.register(Parcel)
class ParcelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'sender', 'weight', 'size', 'status')
    search_fields = ('name', 'sender__email')
    list_filter = ('status',)
    list_per_page = 20
