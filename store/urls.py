from rest_framework.routers import DefaultRouter
from .views import (
    CategoryViewSet,
    ProductViewSet,
    ImageViewSet,
    OrderViewSet,
    CommentViewSet
)

router = DefaultRouter()
router.register('categories', CategoryViewSet)
router.register('products', ProductViewSet)
router.register('images', ImageViewSet)
router.register('orders', OrderViewSet)
router.register('comments', CommentViewSet)

urlpatterns = router.urls
