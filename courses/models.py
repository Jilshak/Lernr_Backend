from django.db import models
from users.models import CustomUser
from django.core.validators import MinValueValidator, MaxValueValidator



# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(blank=True, null=True,
                              upload_to='category_image')

    def __str__(self):
        return self.title


class Courses(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.PositiveIntegerField()
    rating = models.DecimalField(
        blank=True, null=True, decimal_places=2, max_digits=5, default=0)
    no_of_stars = models.PositiveIntegerField(default=0)
    students = models.PositiveIntegerField(default=0)
    no_of_reviews = models.PositiveIntegerField(default=0)
    thumbnail = models.ImageField(blank=True, null=True, upload_to='thumbnail')
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, blank=True, null=True)
    course_length = models.DecimalField(
        blank=True, null=True, decimal_places=2, max_digits=5)
    finished = models.BooleanField(default=False)
    what_you_learn = models.TextField(blank=True, null=True)
    offer_price = models.CharField(blank=True, null=True, max_length=200)
    unlist_course = models.BooleanField(blank=True, null=True, default=False)
    
    have_quiz = models.BooleanField(default=False, blank=True, null=True)

    created_at = models.DateField(auto_now_add=True, null=True, blank=True)

    # payment
    stripe_product_id = models.CharField(max_length=255, blank=True, null=True)

    # requirements
    requirements = models.TextField(blank=True, null=True)
    
    # quiz
    # have_quiz = models.BooleanField(blank=True, null=True, default=False)
    # quiz_completed = models.BooleanField(blank=True, null=True, default=False)

    course_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class CourseVideo(models.Model):
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    video_url = models.CharField(max_length=500, blank=True, null=True)
    video_ref = models.CharField(max_length=1000, blank=True, null=True)
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    

class CourseLessonProgress(models.Model):
    student = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    lesson = models.ForeignKey(CourseVideo, on_delete=models.CASCADE)
    progress = models.IntegerField(
        default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])

    def __str__(self):
        return f'{self.student.email}-{self.lesson.title} Progress'
    

class Reviews(models.Model):
    review_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    review = models.TextField()
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    stars = models.IntegerField(default=1, blank=True, null=True)
    created_at = models.DateField(auto_now_add=True, blank=True, null=True)

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
    progress = models.PositiveIntegerField(blank=True, null=True, default=0)
    got_certificate = models.BooleanField(blank=True, null=True, default=False)
    marks_obtained = models.PositiveIntegerField(blank=True, null=True, default=0)
    created_at = models.DateField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return f'{self.user.email}-{self.course_id.title}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        
        lessons = CourseVideo.objects.filter(course=self.course_id)
        for lesson in lessons:
            CourseLessonProgress.objects.create(
                student=self.user,
                lesson=lesson,
                progress=0
            )
            
class Quiz(models.Model):
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    question = models.CharField(max_length=500, blank=True, null=True)
    option1 = models.CharField(max_length=200, blank=True, null=True)
    option2 = models.CharField(max_length=200, blank=True, null=True)
    option3 = models.CharField(max_length=200, blank=True, null=True)
    option4 = models.CharField(max_length=200, blank=True, null=True)
    correct_anwer = models.PositiveIntegerField(blank=True, null=True)
    
    def __str__(self):
        return self.question