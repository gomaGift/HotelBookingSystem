from datetime import timezone,datetime

from django.db import models
from users.models import User
import random

# Create your models here.


class Facility(models.Model):
    name = models.CharField(max_length=255)
    avatar = models.ImageField(upload_to='Hotel-facilites', null=True, blank=True)

    def __str__(self):
        return self.name

class Hotel(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    description = models.TextField()
    star_rating = models.DecimalField(max_digits=3, decimal_places=1)
    check_in_time = models.TimeField(default='00:00:00')  # 24/7 check-in
    check_out_time = models.TimeField(default='00:00:00')  # 24/7 checkout
    contact_phone = models.CharField(max_length=20)
    contact_email = models.EmailField()
    facilities = models.ManyToManyField(Facility, related_name='facilities')
    

    def __str__(self):
        return self.name
    
class HotelPhoto(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='hotel_photos')
    image = models.ImageField(upload_to='hotel_photos/')   

class Feature(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class RoomType(models.Model):
    name = models.CharField(max_length=50)
    feature = models.ManyToManyField(Feature, related_name='room_features')
    description = models.TextField()
    base_price = models.DecimalField(max_digits=6, decimal_places=2)


    def __str__(self):
        return self.name
    

class Room(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    room_number = models.CharField(max_length=10)
    bed_count = models.PositiveIntegerField()
    price_per_night = models.DecimalField(max_digits=50, decimal_places=2, blank=True)
    room_type = models.ForeignKey(RoomType, on_delete=models.CASCADE, related_name='rooms')
    max_adults = models.PositiveIntegerField(default=1)  # Maximum number of adults allowed
    max_children = models.PositiveIntegerField(default=1)
    max_guests = models.PositiveIntegerField(default=0)
    is_available = models.BooleanField(default=True)
    room_size = models.CharField(max_length=20)
    
    def order_by(self):
        return self.objects.order_by('room_type__name')
    
    def get_display_photo(self):
        # You can customize the logic here to select the display photo
        # For example, to select a random photo, you can use:
        photos = self.room_images.all()
        if photos:
            return random.choice(photos)
        else:
            return None
        





    def __str__(self):
        return f"{self.room_type.name} at {self.hotel.name}"
    
    def save(self, *args, **kwargs):
        # Calculate the room amount based on the room type's base price and the number of beds
        if not self.price_per_night:
            self.price_per_night = self.room_type.base_price * self.bed_count
            super().save(*args, **kwargs)


    
class RoomPhoto(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='room_images')
    photo = models.ImageField(upload_to='room_photos/')

    def __str__(self) -> str:
        return f'{self.room.room_type.name} image'




    


class Review(models.Model):

    RATING = [('1', '★☆☆☆☆'),
              ( '2', '★★☆☆☆'),
              ( '3', '★★★☆☆'),
              ( '4', '★★★★☆'),
              ( '5', '★★★★★'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='room_reviews')
    rating = models.CharField(max_length=5, choices=RATING, blank=True)
    comment = models.CharField(max_length=100, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    class Meta:
        ordering = ('-created',)
     
    def save(self, *args, **kwargs):
        # Calculate the room amount based on the room type's base price and the number of beds
        if self.rating:
            numerical_rating = int(self.rating)
            self.rating = '★' * numerical_rating + '☆' * (5 - numerical_rating)
            super().save(*args, **kwargs)   


    
class Reservation(models.Model):
   RESERVATION_STATUS = [
       ('pay', 'Awaiting Payment'),
       ('pen','Pending'),
       ('can', 'Cancelled'),
       ('book', 'Booked'),
       ('ref', 'Refunded'),
       ('active', 'Active'),
       ('inactive', 'Inactive')

   ]
   user = models.ForeignKey(User, on_delete=models.SET_NULL,null=True, blank=True)
   room = models.ForeignKey(Room, on_delete=models.CASCADE)
   check_in_date = models.DateField()
   check_out_date = models.DateField()
   first_name = models.CharField(max_length=20)
   last_name = models.CharField(max_length=20)
   phone_number = models.CharField(max_length=15)
   email = models.EmailField()
   duration = models.PositiveIntegerField(default=0)
   total_price = models.DecimalField(max_digits=50, decimal_places=2, blank=True, default=0)
   reservation_id = models.CharField(max_length=20, default=0)
   reservation_date = models.DateTimeField(auto_now_add=True)
   reservation_status = models.CharField(max_length=12, choices=RESERVATION_STATUS, default='pay')

   class Meta:
       ordering = ['-reservation_date']

   def save(self, *args, **kwargs):
        # Update the room's availability status when saving the reservation

        # Calculate the difference in days
        if self.phone_number.startswith('0'):
            self.phone_number = '+26' + self.phone_number
        self.duration = (self.check_out_date - self.check_in_date).days
        self.total_price = self.duration * self.room.price_per_night
        self.reservation_id = self.room.room_number + str(self.check_in_date)
        self.room.is_available = False  # Room is reserved
        self.room.save()
        super(Reservation, self).save(*args, **kwargs)
       
        
class Payment(models.Model):
    pass