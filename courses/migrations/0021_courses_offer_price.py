# Generated by Django 4.2.5 on 2023-10-07 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0020_reviews_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='offer_price',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
