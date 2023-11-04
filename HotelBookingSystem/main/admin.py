from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Facility)
admin.site.register(models.Hotel)
admin.site.register(models.HotelPhoto)
admin.site.register(models.Room)
admin.site.register(models.RoomPhoto)
admin.site.register(models.Review)

admin.site.register(models.Payment)
admin.site.register(models.RoomType)
admin.site.register(models.Feature)

@admin.register(models.Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('room', 'user', 'check_in_date', 'check_out_date', 'reservation_status')
    list_filter = ('reservation_status',)


