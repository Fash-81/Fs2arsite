from . import views
from .views import *
from django.urls import path, include
from rest_framework.routers import DefaultRouter




router= DefaultRouter()
router.register('portfolios',PortfolioViewSets,basename='portfolios')
router.register('orders',OrderViewSets,basename='orders')


urlpatterns = [
    path('', include(router.urls)),
    path('', include(router.urls)),
]

