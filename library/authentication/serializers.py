from rest_framework import serializers

from book.serializers import BookSerializer
from order.models import Order
from .models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'

    def create(self, validated_data):
        validated_data.pop("groups")
        validated_data.pop("user_permissions")
        user = CustomUser.objects.create(**validated_data)
        user.set_password(validated_data.get("password"))
        user.save()
        return user


    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.first_name)
        instance.middle_name = validated_data.get('middle_name', instance.middle_name)
        instance.email = validated_data.get('email', instance.email)
        instance.role = validated_data.get('role', instance.role)

        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.is_superuser = validated_data.get('is_superuser', instance.is_superuser)
        instance.is_staff = validated_data.get('is_staff', instance.is_staff)

        instance.set_password(validated_data.get("password", instance.password))

        instance.save()

        return instance


class UserOrdersListSerializer(serializers.ModelSerializer):
    book = BookSerializer(read_only=True)

    # user = UserSerializer(read_only=True)

    class Meta:
        model = Order
        fields = '__all__'
