from django.db import models
import uuid 

# Create your models here.
class Dessert(models.Model):
    identifier = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    category = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    identification = models.TextField(max_length=200)
    initdate = models.CharField(max_length=200)
    productname = models.CharField(max_length=200)
    value = models.PositiveIntegerField()

    def __str__(self):
        return self.productname