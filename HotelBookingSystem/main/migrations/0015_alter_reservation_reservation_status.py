# Generated by Django 4.2.5 on 2023-10-27 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_alter_reservation_reservation_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='reservation_status',
            field=models.CharField(choices=[('pay', 'Awaiting Payment'), ('pen', 'Pending'), ('can', 'Cancelled'), ('book', 'Booked'), ('ref', 'Refunded'), ('active', 'Active'), ('inactive', 'Inactive')], default='pay', max_length=12),
        ),
    ]
