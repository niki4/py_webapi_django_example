from django.conf.urls import url, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'products', views.ProductViewSet)
router.register(r'departments', views.DepartmentViewSet)
router.register(r'features', views.FeatureViewSet)

app_name = 'catalog'
urlpatterns = [
    url(r'^', include(router.urls))
]
