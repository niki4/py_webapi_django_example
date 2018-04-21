from rest_framework import viewsets

from .models import Product, Department, Feature
from .serializers import ProductSerializer, DepartmentSerializer, FeatureSerializer


class ProductViewSet(viewsets.ModelViewSet):
    """ API endpoint that allow CRUD over products """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class DepartmentViewSet(viewsets.ModelViewSet):
    """ API endpoint that allow CRUD over departments """
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class FeatureViewSet(viewsets.ModelViewSet):
    """ API endpoint that allow CRUD over features """
    queryset = Feature.objects.all()
    serializer_class = FeatureSerializer
