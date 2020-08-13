# tests/test_serializers.py
from django.test import TestCase

from ..serializer import DessertSerializer
from .test_factories import DessertFactory

class DessertSerializer(TestCase):
    def test_model_fields(self):
        serializer = DessertSerializer()
        dessert = DessertFactory()
        for field_name in ['identifier', 'category', 'description', 'identification', 'initdate', 'productname', 'value']:
            self.assertEqual(serializer.data[field_name], getattr(dessert, field_name))
