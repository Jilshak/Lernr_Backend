from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import *
from rest_framework.response import Response
import stripe
from rest_framework import status
from django.conf import settings

stripe.api_key = settings.STRIPE_SECRET_KEY


class CoursesViewSet(ModelViewSet):
    serializer_class = CoursesSerializer
    queryset = Courses.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Create the Stripe product
        course_product = stripe.Product.create(
            name=serializer.validated_data['title'],
        )

        course_price = stripe.Price.create(
            product=course_product.id,  # Use the product ID from the previous step
            # Set the price amount here
            unit_amount=serializer.validated_data['price'],
            currency='inr', 
        )

        # Save the Stripe product ID to the course model
        serializer.validated_data['stripe_product_id'] = course_product['id']

        course = serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


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
