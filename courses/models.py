from django.db import models
from users.models import CustomUser


# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(blank=True, null=True, upload_to='category_image')
    
    def __str__(self):
        return self.title


class Courses(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.PositiveIntegerField()
    rating = models.PositiveIntegerField(default=0)
    students = models.PositiveIntegerField(default=0)
    no_of_reviews = models.PositiveIntegerField(default=0)
    thumbnail = models.ImageField(blank=True, null=True, upload_to='thumbnail')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    course_length = models.DecimalField(blank=True, null=True, decimal_places=2, max_digits=5)
    minor_description = models.CharField(max_length=300, blank=True, null=True)
    
    requirements = models.TextField(blank=True, null=True)
    course_by = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    
class Reviews(models.Model):
    review_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    review = models.TextField()
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.review_by.email}-{self.course.title}'
    
class CartItem(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    on_course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.user.email}-{self.on_course.title}'
    
class CoursesBought(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    course_id = models.ForeignKey(Courses, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.user.email}-{self.course_id.title}'