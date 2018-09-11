from rest_framework import serializers
from django.contrib.auth.models import User
from . models import (
    Category,
    Site,
)

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
        )


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = (
            'name',
        )


class SiteSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=True, read_only=True)

    class Meta:
        model = Site
        fields = (
            'id',
            'name',
            'url',
            'category',
            'description',
            'timestamp',
            'updated',
        )

