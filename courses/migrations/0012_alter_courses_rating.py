# Generated by Django 4.2.5 on 2023-10-02 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0011_rename_no_of_rating_courses_no_of_stars'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='rating',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5, null=True),
        ),
    ]
