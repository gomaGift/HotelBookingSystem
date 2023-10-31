# Generated by Django 4.2.5 on 2023-09-17 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='max_guests',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='room',
            name='max_adults',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
