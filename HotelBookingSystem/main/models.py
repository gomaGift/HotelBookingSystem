from django.db import models
from users.models import User

# Create your models here.


class Hotel(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    description = models.TextField()
    star_rating = models.DecimalField(max_digits=3, decimal_places=1)
    check_in_time = models.TimeField(default='00:00:00')  # 24/7 check-in
    check_out_time = models.TimeField(default='00:00:00')  # 24/7 checkout
    price_range = models.CharField(max_length=50)
    contact_phone = models.CharField(max_length=20)
    contact_email = models.EmailField()
    gallery = models.ImageField(upload_to='hotel_photos/')

    def __str__(self):
        return self.name
    

class Room(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    room_number = models.CharField(max_length=10)
    bed_count = models.PositiveIntegerField()
    price_per_night = models.DecimalField(max_digits=6, decimal_places=2)
    room_type = models.CharField(max_length=50)
    description = models.TextField()
    is_available = models.BooleanField(default=True)
    photo = models.ImageField(upload_to='room_photos/')
    

    # Other room attributes...

    def __str__(self):
        return f"Room {self.room_number} at {self.hotel.name}"
    
    
class Reservation(models.Model):
    pass


class Review(models.Model):
    pass


class Payment(models.Model):
    pass