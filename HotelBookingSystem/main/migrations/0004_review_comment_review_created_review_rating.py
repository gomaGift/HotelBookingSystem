# Generated by Django 4.2.5 on 2023-09-21 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_facility_avatar_alter_hotel_facilities_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='comment',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='review',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='review',
            name='rating',
            field=models.CharField(blank=True, choices=[('1', '★☆☆☆☆'), ('2', '★★☆☆☆'), ('3', '★★★☆☆'), ('4', '★★★★☆'), ('5', '★★★★★')], max_length=5),
        ),
    ]
