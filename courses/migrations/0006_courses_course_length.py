# Generated by Django 4.2.5 on 2023-09-26 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_category_image_alter_courses_no_of_reviews'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='course_length',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=2, null=True),
        ),
    ]
