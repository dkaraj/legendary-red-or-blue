from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views.property_views import PropertyViewSet
app_name='api'
router = DefaultRouter()

router.register(r'property', PropertyViewSet, basename='property')

urlpatterns = [
    path("", include(router.urls)),
]
