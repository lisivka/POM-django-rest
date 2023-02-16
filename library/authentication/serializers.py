from rest_framework import serializers

from book.serializers import BookSerializer
from order.models import Order
from .models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'


# class UserListSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CustomUser
#         fields = ['first_name', 'last_name', 'middle_name', 'email', 'password', 'updated_at', 'created_at',
#                   'role', 'is_active']


class UserOrdersListSerializer(serializers.ModelSerializer):
    book = BookSerializer(read_only=True)

    class Meta:
        model = Order
        fields = '__all__'
