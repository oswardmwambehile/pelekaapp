# urls.py
from django.urls import path
from .views import (
    TransportCompanyCreateView,
    TransportCompanyDetailView,
    TransportCompanyUpdateView,
    TransportCompanyDeleteView,
    TransportCompanyListView,
    VehicleCreateView,
    VehicleDetailView,
    VehicleUpdateView,
    VehicleDeleteView,
    VehicleListView,
)
urlpatterns = [
    path('transport-company/create/', TransportCompanyCreateView.as_view(), name='transport-company-create'),
    path('transport-company/<int:pk>/', TransportCompanyDetailView.as_view(), name='transport-company-detail'),
    path('transport-company/<int:pk>/update/', TransportCompanyUpdateView.as_view(), name='transport-company-update'),
    path('transport-company/<int:pk>/delete/', TransportCompanyDeleteView.as_view(), name='transport-company-delete'),
    
    path('transport-company/', TransportCompanyListView.as_view(), name='transport-company-list'),

    path('vehicles/', VehicleListView.as_view(), name='vehicle-list'),
    path('vehicles/create/', VehicleCreateView.as_view(), name='vehicle-create'),
    path('vehicles/<int:pk>/', VehicleDetailView.as_view(), name='vehicle-detail'),
    path('vehicles/<int:pk>/update/', VehicleUpdateView.as_view(), name='vehicle-update'),
    path('vehicles/<int:pk>/delete/', VehicleDeleteView.as_view(), name='vehicle-delete'),
]
