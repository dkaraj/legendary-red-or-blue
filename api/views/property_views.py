from django.contrib.auth.models import User
from rest_framework import generics, viewsets
from rest_framework.permissions import AllowAny

from api.models import Property
from api.serializers.property_serializers import PropertySerializer


class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    permission_classes = (AllowAny,)
