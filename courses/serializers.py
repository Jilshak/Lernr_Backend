from .models import *
from rest_framework.serializers import ModelSerializer
from users.serializers import UserSerializer

class CoursesSerializer(ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Courses
        
        
class ReviewSerializer(ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Reviews
        
        
class CartItemSerializer(ModelSerializer):
    class Meta:
        fields = '__all__'
        model = CartItem
        
        
class CategorySerializer(ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Category
        
        
class CoursesBoughtSerializer(ModelSerializer):
    class Meta:
        fields = '__all__'
        model = CoursesBought