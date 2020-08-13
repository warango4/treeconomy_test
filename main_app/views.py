import requests
from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from .services import get_products, post_products, put_products, delete_products
from .models import Dessert
from .serializer import DessertSerializer

@api_view(['GET', 'POST'])
def product_list(request):
   """
   List all products or create a new one
   """
   if request.method == 'GET':
      products_list = get_products()
      total_value = sum(int(value['value']) for value in products_list.values() if 'value' in value)
      return render(request, "main_app/home.html", {"products": products_list, "total_value" : total_value})

   elif request.method == 'POST':
      post_product = post_products(request.data)
      return Response(request.data, post_product.status_code)

@api_view(['PUT', 'DELETE'])
def product_modification(request):
   if request.method == 'PUT':
      put_product = put_products(request.data)
      return Response(request.data, put_product.status_code)

   if request.method == 'DELETE':
      delete_product = delete_products(request.data)
      return Response(request.data, delete_product.status_code)

class DessertViewSet(viewsets.ModelViewSet):
   serializer_class = DessertSerializer
   queryset = Dessert.objects.all()