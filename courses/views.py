from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import *

class CoursesViewSet(ModelViewSet):
    serializer_class = CoursesSerializer
    queryset = Courses.objects.all()
    
class ReviewViewSet(ModelViewSet):
    serializer_class = ReviewSerializer
    queryset = Reviews.objects.all()
    
class CartItemViewSet(ModelViewSet):
    serializer_class = CartItemSerializer
    queryset = CartItem.objects.all()
    
    
class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    
    
class CoursesBoughtViewSet(ModelViewSet):
    serializer_class = CoursesBoughtSerializer
    queryset = CoursesBought.objects.all()
    
    
