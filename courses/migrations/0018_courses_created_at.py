# Generated by Django 4.2.5 on 2023-10-06 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0017_coursesbought_progress'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='created_at',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
