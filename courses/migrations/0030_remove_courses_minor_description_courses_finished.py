# Generated by Django 4.2.5 on 2023-10-12 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0029_courses_have_quiz_courses_quiz_completed_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courses',
            name='minor_description',
        ),
        migrations.AddField(
            model_name='courses',
            name='finished',
            field=models.BooleanField(default=False),
        ),
    ]
