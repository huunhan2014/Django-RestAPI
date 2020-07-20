from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Post, Type, Product, FieldPlanningRun


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups', 'is_staff']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class TypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Type
        fields = '__all__'


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ('type_id', 'name', 'price', 'quantity', 'description')


class FieldPlanningRunSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FieldPlanningRun
        fields = '__all__'
