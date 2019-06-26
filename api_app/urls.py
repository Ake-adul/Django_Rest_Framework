from django.urls import path, include
from . import views
from rest_framework import routers

routers = routers.DefaultRouter()
routers.register('product', views.ProductViewSet)
routers.register('category', views.CategoryViewSet)

urlpatterns = [
    path('', include(routers.urls))
]