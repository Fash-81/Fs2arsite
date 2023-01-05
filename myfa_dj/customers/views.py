from django.shortcuts import render, redirect
from rest_framework import viewsets
from rest_framework.response import Response
from .models import *
from .serializers import *


class OrderViewSets(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

    def perform_create(self, serializer):
        return serializer.save(customer=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(customer=self.request.user)


class PortfolioViewSets(viewsets.ModelViewSet):
    serializer_class = PortfolioSerializer
    queryset = Portfolio.objects.all()
