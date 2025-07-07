from django.contrib import admin
from .models import Payment

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'booking', 'amount', 'payment_method', 'transaction_id', 'status', 'timestamp')
    search_fields = ('transaction_id', 'payment_method', 'booking__id')
    list_filter = ('status', 'payment_method')
    list_per_page = 20
