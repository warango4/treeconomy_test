from django.test import TestCase
from django.urls import reverse
from rest_framework import status

from .test_factories import DessertFactory, UserFactory

class CompanyViewSetTestCase(TestCase):
    def setup(self):
        self.user = UserFactory(email='')