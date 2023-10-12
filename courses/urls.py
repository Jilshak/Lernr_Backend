from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('course', CoursesViewSet, basename='course_view')
router.register('review', ReviewViewSet, basename='review_view')
router.register('cartItem', CartItemViewSet, basename='cartItem_view')
router.register('category', CategoryViewSet, basename='category_view')
router.register('bought_courses', CoursesBoughtViewSet, basename='bought_courses')
router.register('course_video', CourseVideoViewSet, basename='course_video')
router.register('course_lessons', CourseLessonProgressViewSet, basename='course_lesson_progress')
router.register('quiz', QuizViewSet, basename='quiz')

urlpatterns = [
    
]

urlpatterns += router.urls
