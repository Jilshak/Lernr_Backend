from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('course', CoursesViewSet, basename='course_view')
router.register('review', ReviewViewSet, basename='review_view')
router.register('cartItem', CartItemViewSet, basename='cartItem_view')
router.register('category', CategoryViewSet, basename='category_view')

urlpatterns = [
    
]

urlpatterns += router.urls