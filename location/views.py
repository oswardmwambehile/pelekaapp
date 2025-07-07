from rest_framework import generics, permissions
from .models import Region, District
from .serializers import RegionSerializer, DistrictSerializer
from .permissions import IsOwner

# --- Region Views ---

class RegionListView(generics.ListAPIView):
    serializer_class = RegionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Region.objects.filter(user=self.request.user)

class RegionCreateView(generics.CreateAPIView):
    serializer_class = RegionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class RegionDetailView(generics.RetrieveAPIView):
    serializer_class = RegionSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    def get_queryset(self):
        return Region.objects.filter(user=self.request.user)

class RegionUpdateView(generics.UpdateAPIView):
    serializer_class = RegionSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    def get_queryset(self):
        return Region.objects.filter(user=self.request.user)

class RegionDeleteView(generics.DestroyAPIView):
    serializer_class = RegionSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    def get_queryset(self):
        return Region.objects.filter(user=self.request.user)

# --- District Views ---

class DistrictListView(generics.ListAPIView):
    serializer_class = DistrictSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return District.objects.filter(user=self.request.user)

class DistrictCreateView(generics.CreateAPIView):
    serializer_class = DistrictSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class DistrictDetailView(generics.RetrieveAPIView):
    serializer_class = DistrictSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    def get_queryset(self):
        return District.objects.filter(user=self.request.user)

class DistrictUpdateView(generics.UpdateAPIView):
    serializer_class = DistrictSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    def get_queryset(self):
        return District.objects.filter(user=self.request.user)

class DistrictDeleteView(generics.DestroyAPIView):
    serializer_class = DistrictSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    def get_queryset(self):
        return District.objects.filter(user=self.request.user)


from rest_framework import generics, permissions
from .models import Route
from .serializers import RouteSerializer
from .permissions import IsOwner  # your custom permission

class RouteCreateView(generics.CreateAPIView):
    serializer_class = RouteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_context(self):
        return {'request': self.request}

class RouteListView(generics.ListAPIView):
    serializer_class = RouteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Route.objects.filter(user=self.request.user)

class RouteDetailView(generics.RetrieveAPIView):
    serializer_class = RouteSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    def get_queryset(self):
        return Route.objects.filter(user=self.request.user)

class RouteUpdateView(generics.UpdateAPIView):
    serializer_class = RouteSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    def get_queryset(self):
        return Route.objects.filter(user=self.request.user)

class RouteDeleteView(generics.DestroyAPIView):
    serializer_class = RouteSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    def get_queryset(self):
        return Route.objects.filter(user=self.request.user)
