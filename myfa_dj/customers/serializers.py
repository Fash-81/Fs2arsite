from rest_framework import serializers
from .models import *



class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model= Portfolio
        read_only_fields=('created_at',),
        fields=(
            'case',
            'topic',
            'subject',
            'content',
            'description',
            'p_image',
        )
    
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model= Order
        read_only_fields=('created_at',),
        fields=(
            'case',
            'topic',
            'subject',
            'content',
            'description',
            'o_image',
        )

