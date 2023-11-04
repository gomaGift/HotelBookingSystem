from django.urls import path
from . import views


urlpatterns = [
   path('', views.home, name='landing-page'),
   path('dashboard', views.dashboard, name='dashboard'),
   path('rooms/', views.rooms, name='rooms'),
   path('search-room/', views.rooms, name='search-rooms'),
   path('room/<int:id>', views.room_detail, name='room-detail'),
   path('pay/<int:id>', views.pay, name='pay-now'),
   path('check-in/<int:id>', views.check_in, name='check-in'),
   path('check-out/<int:id>', views.check_out, name='check-out'),
   path('room-availability-rooms/', views.check_room, name='check-availability-rooms'),
   path('reservation-summary/<str:id>', views.gen_reservation_summary, name='gen-reservation-summary'),
   path('find-reservation/', views.find_reservation, name='find-reservations'),
   path('room-availability/', views.check_room_availability, name='check-availability'),
   path('book_room/<int:id>', views.book_room, name='book'),
   path('bookings/<int:id>/', views.my_bookings, name='my-bookings'),
   path('cancel/<int:id>', views.cancel_reservation, name='cancel'),
   path('contact/', views.contact, name='contact-us'),
   path('facility/', views.facility, name='facilities'),
   path('about/', views.about, name='about-us'),
   path('rate-room/<int:id>', views.rate_room , name='rate-room'),


]
