# Generated by Django 4.2.5 on 2023-10-03 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_alter_reservation_check_in_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='duration',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='reservation',
            name='reservation_id',
            field=models.CharField(default=0, max_length=20),
        ),
        migrations.AddField(
            model_name='reservation',
            name='total_price',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=50),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='reservation_status',
            field=models.CharField(choices=[('pay', 'Awaiting Payment'), ('pen', 'Pending'), ('can', 'Cancelled'), ('book', 'Booked'), ('ref', 'Refunded')], default='pay', max_length=50),
        ),
        migrations.AlterField(
            model_name='room',
            name='price_per_night',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=50),
        ),
    ]
