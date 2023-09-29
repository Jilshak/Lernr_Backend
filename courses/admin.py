from django.contrib import admin
from .models import *



# Register your models here.
admin.site.register(Courses)
admin.site.register(CartItem)
admin.site.register(Reviews)
admin.site.register(Category)
admin.site.register(CoursesBought)