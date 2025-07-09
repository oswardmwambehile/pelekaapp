from django.urls import path
from . import views

urlpatterns = [
    path('make/<int:booking_id>/', views.make_payment, name='make-payment'),
    path('my-payments/', views.list_user_payments, name='user-payments'),
    path('update-status/<int:payment_id>/', views.update_payment_status, name='update-payment-status'),
]
