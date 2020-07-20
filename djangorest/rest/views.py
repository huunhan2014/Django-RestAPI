from rest_framework.generics import (ListCreateAPIView, RetrieveUpdateDestroyAPIView,)
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Post, Type, Product, FieldPlanningRun
from rest_framework import permissions
from django.contrib.auth.models import User, Group
from .serializers import UserSerializer, GroupSerializer, PostListSerializer, TypeSerializer, ProductSerializer, FieldPlanningRunSerializer



class PostDetailUpdateAPIView(viewsets.GenericViewSet,
                              RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer
    lookup_field = 'id'


class PostListCreateAPIView(viewsets.GenericViewSet,
                            ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer
    permission_classes = [IsAuthenticated]


class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all().order_by('-username')
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):

    queryset = Group.objects.all().order_by('-name')
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class TypeViewSet(viewsets.ModelViewSet):
    queryset = Type.objects.all().order_by('-name')
    serializer_class = TypeSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('-name')
    serializer_class = ProductSerializer


class FieldPlanningRunViewSet(viewsets.ModelViewSet):
    queryset = FieldPlanningRun.objects.all()
    serializer_class = FieldPlanningRunSerializer
