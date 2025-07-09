from django.urls import path
from . import views
from .views import booking_create, booking_list, company_bookings, update_company_booking_status

urlpatterns = [
    path('api/schedules/', views.ScheduleListAPIView.as_view(), name='schedule-list'),
    path('api/schedules/create/', views.ScheduleCreateAPIView.as_view(), name='schedule-create'),
    path('api/schedules/<int:pk>/', views.ScheduleDetailAPIView.as_view(), name='schedule-detail'),
    path('api/schedules/<int:pk>/update/', views.ScheduleUpdateAPIView.as_view(), name='schedule-update'),
    path('api/schedules/<int:pk>/delete/', views.ScheduleDeleteAPIView.as_view(), name='schedule-delete'),
    path('bookings/create/', booking_create, name='booking-create'),
    path('bookings/', booking_list, name='booking-list'),
    path('company/bookings/', company_bookings, name='company-bookings'),
    path('company/bookings/<int:booking_id>/status/', update_company_booking_status, name='company-booking-status-update'),
]
