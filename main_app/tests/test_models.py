from django.test import TestCase

from ..models import Dessert
from .test_factories import DessertFactory

class DessertTestCase(TestCase):
    def test_str(self):
        dessert = DessertFactory()
        self.assertEqual(str(dessert), dessert.productname)