from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from api.models import Property


class PropertyTests(APITestCase):
    def setUp(self):
        self.data = {
            "property_address": "test",
            "listing_price": 11,
        }
        self.response = self.client.post(
            reverse('api:property-list'),
            self.data,
            format="json")

    def test_create_property(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Property.objects.count(), 1)
        self.assertEqual(Property.objects.get().property_address, 'test')

    def test_api_list_properties(self):
        url = reverse('api:property-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Property.objects.count(), 1)

    def test_get_property_by_id(self):
        property = Property.objects.get()
        response = self.client.get(
            reverse('api:property-detail',
                    kwargs={'pk': property.id}), format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_property(self):
        property = Property.objects.get()
        new_data = {
            "property_address": "test_updated",
            "listing_price": 11,
        }
        response = self.client.put(
            reverse('api:property-detail',
                    kwargs={'pk': property.id}), data=new_data, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Property.objects.get().property_address, 'test_updated')

    def test_delete_property(self):
        property = Property.objects.get()
        response = self.client.delete(
            reverse('api:property-detail',
                    kwargs={'pk': property.id}), format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Property.objects.count(), 0)
