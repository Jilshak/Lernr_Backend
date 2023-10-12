from .models import *
from rest_framework.serializers import ModelSerializer

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
        
class CourseVideosSerializer(ModelSerializer):
    class Meta:
        fields = '__all__'
        model = CourseVideo
        
        
class CourseLessonProgressSerializer(ModelSerializer):
    class Meta:
        fields = '__all__'
        model = CourseLessonProgress
        
        
class QuizSerializer(ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Quiz