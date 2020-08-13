from django.conf.urls import include, re_path
from rest_framework.routers import DefaultRouter
from .views import DessertViewSet, product_list, product_modification
from django.urls import include, path

router = DefaultRouter()
router.register(r'desserts', DessertViewSet, basename="Desserts")
#router.register(r'products', ProductsViewSet, basename="Products")

urlpatterns = [
    path('get_post', product_list),
    path('', include(router.urls)),
    path('put_delete', product_modification),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]