from factory import DjangoModelFactory, Faker, LazyFunction
from ..models import Dessert 
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User

class DessertFactory(DjangoModelFactory):
    category = Faker('Postres')
    description = Faker('prueba postre para la tarde')
    identification = Faker('B01')
    initdate = Faker('11-06-2019')
    productname = Faker('Postre Brazo de Reina')
    value = Faker(3700)

    class Meta:
        model = Dessert

class UserFactory(DjangoModelFactory):
    first_name = Faker('first_name')
    last_name = Faker('last_name')
    email = Faker('email')
    password = LazyFunction(lambda: make_password('pi3.1415'))
    
    class Meta:
        model = User