from django.urls import path
from .views import (
    RegionListView, RegionCreateView, RegionDetailView, RegionUpdateView, RegionDeleteView,
    DistrictListView, DistrictCreateView, DistrictDetailView, DistrictUpdateView, DistrictDeleteView,
    RouteCreateView,
    RouteListView,
    RouteDetailView,
    RouteUpdateView,
    RouteDeleteView,
)
from .views import search_routes
urlpatterns = [
   
    # Region URLs
    path('regions/', RegionListView.as_view(), name='region-list'),
    path('regions/create/', RegionCreateView.as_view(), name='region-create'),
    path('regions/<int:pk>/', RegionDetailView.as_view(), name='region-detail'),
    path('regions/<int:pk>/update/', RegionUpdateView.as_view(), name='region-update'),
    path('regions/<int:pk>/delete/', RegionDeleteView.as_view(), name='region-delete'),

    # District URLs
    path('districts/', DistrictListView.as_view(), name='district-list'),
    path('districts/create/', DistrictCreateView.as_view(), name='district-create'),
    path('districts/<int:pk>/', DistrictDetailView.as_view(), name='district-detail'),
    path('districts/<int:pk>/update/', DistrictUpdateView.as_view(), name='district-update'),
    path('districts/<int:pk>/delete/', DistrictDeleteView.as_view(), name='district-delete'),


    path('routes/', RouteListView.as_view(), name='route-list'),
    path('routes/create/', RouteCreateView.as_view(), name='route-create'),
    path('routes/<int:pk>/', RouteDetailView.as_view(), name='route-detail'),
    path('routes/<int:pk>/update/', RouteUpdateView.as_view(), name='route-update'),
    path('routes/<int:pk>/delete/', RouteDeleteView.as_view(), name='route-delete'),
    path('routes/search/', search_routes, name='route-search'),
]

