# Generated by Django 4.2.5 on 2023-09-23 11:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_review_rating_alter_review_room'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='review',
            options={'ordering': ('-created',)},
        ),
    ]