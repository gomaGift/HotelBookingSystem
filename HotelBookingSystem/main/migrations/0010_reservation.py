# Generated by Django 4.2.5 on 2023-09-28 14:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0009_delete_reservation'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_in_date', models.DateField(blank=True)),
                ('check_out_date', models.DateField(blank=True)),
                ('reservation_date', models.DateField(auto_now=True)),
                ('reservation_status', models.CharField(choices=[('pay', 'Awaiting Payment'), ('pen', 'Pending'), ('can', 'Cancelled'), ('book', 'Booked'), ('ref', 'Refunded')], max_length=50)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.room')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]