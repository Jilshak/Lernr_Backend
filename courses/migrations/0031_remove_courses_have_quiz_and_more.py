# Generated by Django 4.2.5 on 2023-10-14 04:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0030_remove_courses_minor_description_courses_finished'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courses',
            name='have_quiz',
        ),
        migrations.RemoveField(
            model_name='courses',
            name='quiz_completed',
        ),
    ]
