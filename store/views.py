from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from rest_framework.permissions import IsAuthenticated
from .models import Category, Product, Image, Order, Comment
from .serializers import (
    CategorySerializer,
    ProductSerializer,
    ImageSerializer,
    OrderSerializer,
    CommentSerializer,
    LikeSerializer,
    Like
)

# Create your views here.

@method_decorator(cache_page(60 * 5), 'list')
class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.prefetch_related('products')
    serializer_class = CategorySerializer



class ProductViewSet(ModelViewSet):
    queryset = Product.objects.select_related('category') \
        .prefetch_related('images', 'comments')
    serializer_class = ProductSerializer

class ImageViewSet(ModelViewSet):
    queryset = Image.objects.select_related('product')
    serializer_class = ImageSerializer


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.select_related('product', 'user')
    serializer_class = CommentSerializer

class LikeViewSet(ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
