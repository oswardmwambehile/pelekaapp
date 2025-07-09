from django.db import models
from django.conf import settings

class Region(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)  # set on create
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)      # updated on every save

    def __str__(self):
        return self.name

class District(models.Model):
    name = models.CharField(max_length=100)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='districts')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        verbose_name_plural = "disticts"

    def __str__(self):
        return self.name

from django.db import models
from django.conf import settings



class Route(models.Model):
    origin = models.ForeignKey(
        'District',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='route_origins'
    )
    destination = models.ForeignKey(
        'District',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='route_destinations'
    )
    distance = models.FloatField()
    expected_time = models.DurationField()

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        origin_name = self.origin.name if self.origin else "Unknown"
        destination_name = self.destination.name if self.destination else "Unknown"
        return f"{origin_name} → {destination_name}"