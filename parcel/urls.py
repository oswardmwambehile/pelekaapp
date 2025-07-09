# parcel/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.list_parcels, name='list-parcels'),
    path('add/', views.add_parcel, name='add-parcel'),
    path('view/<int:pk>/', views.view_parcel, name='view-parcel'),
    path('update/<int:pk>/', views.update_parcel, name='update-parcel'),
    path('delete/<int:pk>/', views.delete_parcel, name='delete-parcel'),
]
