# Generated by Django 4.2.5 on 2023-10-09 18:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0024_alter_coursevideo_video_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courses',
            name='video',
        ),
    ]
