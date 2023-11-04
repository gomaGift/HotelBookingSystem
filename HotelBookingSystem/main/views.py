import datetime
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from . import models
from django.views.generic import View
from .models import Reservation, Room, Hotel,Feature
from . forms import RatingForm, RoomFilterForm, AvailabilityCheckForm, ReservationForm, FindReservationForm
from django.urls import reverse
from django.db.models import Q
from django.contrib import messages
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from users.models import User
from django import template


# Create your views here.



def dashboard(request):
    if request.user.user_role == 'sys_admin':
       bookings = Reservation.objects.all()
       my_users = User.objects.all()
       pending = Reservation.objects.filter(reservation_status='pay')
    

       context = {
           'bookings': bookings,
           'my_users': my_users,
           'pending': pending
       }
       return render(request, 'main/dashboard.html', context)


def home(request):
    rooms = Room.objects.all()[:3]
    hotel = Hotel.objects.get(id=1)
    hotel_photos = hotel.hotel_photos.all()
    facilities = hotel.facilities.all()[:5]
    context = {
        'rooms': rooms,
        'hotel_photos': hotel_photos,
        'facilities': facilities
    }
    return render(request, 'main/index.html', context)


def rooms(request):
    form = RoomFilterForm()
    q = request.GET.get('q')
    if q:
        rooms = Room.objects.filter(
            Q(room_type__name__icontains=q)    
        )

    elif request.method == 'POST':
        form = RoomFilterForm(request.POST)
        if form.is_valid():
            selected_features = form.cleaned_data.get('features')
            adults_count = form.cleaned_data.get('adults_count')
            children_count = form.cleaned_data.get('children_count')
            bed_count = form.cleaned_data.get('bed_count')
            room_filters = Q()
            if selected_features:
                room_filters |= Q(room_type__feature__in=selected_features)
            if adults_count:
                room_filters &= Q(max_adults__gte=adults_count)
            if children_count:
                room_filters &= Q(max_children__gte=children_count)
            if bed_count:
                room_filters &= Q(bed_count__gte=bed_count)

            rooms = Room.objects.filter(room_filters).distinct()

        else:
            rooms= Room.objects.order_by('room_type__name')
    else:
        rooms= Room.objects.order_by('room_type__name')
        

    context = {
            'rooms': rooms,
            'form': form
            
        }
    return render(request, 'main/rooms.html', context)


def room_detail(request, id):
    room = Room.objects.get(id=id)
    reviews = room.room_reviews.all()
    context = {'room': room,
               'reviews': reviews
               }
    return render(request, 'main/room_detail.html',context )

def book_room(request, id):
    room = Room.objects.get(id=id)
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            check_in = form.cleaned_data['check_in_date']
            check_out = form.cleaned_data['check_out_date']
            if check_in <= check_out and check_in >= datetime.date.today():
              if Reservation.objects.filter(Q(room=room) & Q(check_in_date__lte=check_out) & Q(check_out_date__gte=check_in) & ~Q(reservation_status='can')):
                  messages.success(request, 'Room unavailable for the chosen period')
                  form = ReservationForm()
                  
              else:
                reservation = form.save(commit=False)
                 

                if request.user.is_authenticated:
                    reservation.user = request.user
                    reservation.room = room
                    reservation.save()
                    url = reverse('my-bookings', kwargs={'id': request.user.id})
                    messages.success(request, 'reservation made successfully')
                    return redirect(url)
                else:
                     reservation.room = room
                     reservation.save()
                     reservation = Reservation.objects.filter(room=room, check_in_date=check_in)[0]
                     return render(request, 'main/comfirm.html', {'reservation': reservation})
                             
            else:
                messages.error(request, 'check-in-date must be less than check-out-date ')
                messages.error(request, 'check in date must be today or any later date')
                form = ReservationForm()
        else:
            form = ReservationForm()
            
    else:
       
        form = ReservationForm()

    return render(request, 'main/book_room.html', {'room': room, 'form': form})

def pay(request, id):
    reservation = Reservation.objects.filter(room_id = id)[0]
    reservation.reservation_status = 'book'
    reservation.save()
    if request.user.is_authenticated:
        url = reverse('my-bookings', kwargs={'id': request.user.id})
        messages.success(request, 'payment successful')
        return redirect(url)
    else:
        return render(request, 'main/comfirm.html', {'reservation': reservation})



def check_in(request, id):
    reservation = Reservation.objects.filter(room_id = id)[0]
    if datetime.date.today() >= reservation.check_in_date and datetime.date.today() <= reservation.check_out_date:
        reservation.reservation_status = 'active'
        reservation.save()
        url = reverse('my-bookings', kwargs={'id': request.user.id})
        messages.success(request, 'Checked in')
        return redirect(url)
    previous_page = request.META.get('HTTP_REFERER')            
    messages.error(request, 'check in only allowed on reservation check in date or later')
    return redirect(previous_page)


def check_out(request, id):
    reservation = Reservation.objects.filter(id=id)[0]
    reservation.room.is_available = True
    reservation.reservation_status = 'inactive'
    reservation.save()
    url = reverse('my-bookings', kwargs={'id': request.user.id})
    messages.success(request, 'Checked out successfully')
    return redirect(url)

def check_room_availability(request):
    q = request.GET.get('q')
    if q:
        rooms = Room.objects.filter(
            Q(room_type__name__icontains=q)    
        )

    if request.method == 'POST':
        form = AvailabilityCheckForm(request.POST)
        if form.is_valid():
            check_in_date = form.cleaned_data.get('check_in_date')
            check_out_date = form.cleaned_data.get('check_out_date')
            if check_in_date <= check_out_date and check_in_date >= datetime.date.today():
                adults = form.cleaned_data.get('adults_count')
                children_count = form.cleaned_data.get('children_count')
                excluded_statuses = ['pay', 'active', 'book']
               
                booked_rooms = Room.objects.filter(
                                                    Q(reservation__check_in_date__lte=check_out_date) &
                                                    Q(reservation__check_out_date__gte=check_in_date) &
                                                    Q(reservation__reservation_status__in=excluded_statuses)
                                                )
                rooms = Room.objects.exclude(id__in=booked_rooms)

                if adults or children_count:
                    available_rooms = []
                    for room in rooms:
                        if room.max_adults >= adults and room.max_children >= children_count:
                            available_rooms.append(room)
                else:
                    available_rooms = rooms
                

            
                form = RoomFilterForm()
                return render(request, 'main/rooms.html', {'available_rooms': available_rooms, 'form': form})
            else:
                previous_page = request.META.get('HTTP_REFERER', '/')
                
                messages.error(request, 'check-in-date must be less than check-out-date ')
                messages.error(request, 'check in date must be today or any later date')
                
                return redirect(previous_page)

                
        else:
           return redirect('landing-page' )

    else:
        form = AvailabilityCheckForm()
    return render(request, 'main/rooms.html', {'rooms': rooms})


def check_room(request):
    q = request.GET.get('q')
    if q:
        rooms = Room.objects.filter(
            Q(room_type__name__icontains=q)    
        )

    if request.method == 'POST':
        form = AvailabilityCheckForm(request.POST)
        if form.is_valid():
            check_in_date = form.cleaned_data.get('check_in_date')
            check_out_date = form.cleaned_data.get('check_out_date')
            excluded_statuses = ['pay', 'active', 'book']
            if check_in_date <= check_out_date and check_in_date >= datetime.date.today():
                           
                booked_rooms = Room.objects.filter(
                                                    Q(reservation__check_in_date__lte=check_out_date) &
                                                    Q(reservation__check_out_date__gte=check_in_date) &
                                                    Q(reservation__reservation_status__in=excluded_statuses)
                                                )
                available_rooms = Room.objects.exclude(id__in=booked_rooms)
                form = RoomFilterForm()
                return render(request, 'main/rooms.html', {'available_rooms': available_rooms, 'form': form})
            
            else:
                messages.error(request, 'check-in-date must be less than check-out-date')
                messages.error(request, 'check in date must be today or any later date')
                return redirect('rooms')
   
        else:
           return redirect('landng-page')

    else:
        form = AvailabilityCheckForm()
    return render(request, 'main/rooms.html', {'form': form, 'rooms': rooms})
            
def my_bookings(request, id):
    reservations = models.Reservation.objects.filter(user_id = id)
    return render(request, 'main/bookings.html', {'reservations': reservations})

def rate_room(request, id):
    room = Room.objects.get(id=id)
    if request.method == 'POST':
        form = RatingForm(request.POST)
        print(form)
        if form.is_valid():
            rating = form.save(commit=False)
            rating.user = request.user
            rating.room = room
            
            rating.save()
            url = reverse('room-detail', kwargs={'id':id})
            return redirect(url)

    else:
     form = RatingForm()
     return render(request, 'main/review.html', {'form': form, 'room': room})


def contact(request):
    return render(request, 'main/contacts.html')

def facility(request):
    hotel = Hotel.objects.get(id=1)
    facilities = hotel.facilities.all()[:5]
    context = {
        'facilities': facilities
    }
    return render(request, 'main/facilities.html', context)


def about(request):
    return render(request, 'main/about.html')

def gen_reservation_summary(request, id):
    reservation = Reservation.objects.filter(id=id)[0]
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename=reservation_summary_{id}.pdf'

    # Create a canvas for the PDF
    p = canvas.Canvas(response)

    # Start creating the PDF content
    p.setFont("Helvetica", 12)
    p.drawString(100, 750, "Reservation Summary")
    p.drawString(100, 730, f"Reservation ID: {reservation.reservation_id}")
    p.drawString(100, 710, f"Guest Name: {reservation.first_name} {reservation.last_name}")
    p.drawString(100, 690, f"Check-In Date: {reservation.check_in_date}")
    p.drawString(100, 690, f"Email: {reservation.email}")
    p.drawString(100, 690, f"Email: {reservation.phone_number}")
    p.drawString(100, 670, f"Check-Out Date: {reservation.check_out_date}")
    # Add more reservation details as needed

    # Save the PDF
    p.showPage()
    p.save()

    return response

def find_reservation(request):
    if request.method == 'POST':
       form = FindReservationForm(request.POST)
       if form.is_valid():
           reservation_id = form.cleaned_data['reservation_id']
           phone_email = form.cleaned_data['phone_email']
           if phone_email.startswith('0'):
             phone_email = '+26' + phone_email
             reservation_query= Reservation.objects.filter(phone_number=phone_email, reservation_id=reservation_id)
             exist = reservation_query.exists()
             if exist:
              reservation = reservation_query[0]
              return render(request, 'main/paid_reservations.html', {'reservation': reservation, 'exists': exist})
           else:
            reservation_query = Reservation.objects.filter(email=phone_email, reservation_id=reservation_id)
            exist = reservation_query.exists()
            if exist:
              reservation = reservation_query[0]
              return render(request, 'main/paid_reservations.html', {'reservation': reservation, 'exist': exist})
           return render(request,'main/paid_reservations.html', {'exist': exist})           

    else:
        form = FindReservationForm()
        return render(request, 'main/find_reservation.html', {'form': form})

def cancel_reservation(request, id):
    reservation = Reservation.objects.filter(id=id)[0]
    reservation.reservation_status = 'can'
    room = reservation.room
    room.is_available = True
    room.save()
    reservation.save()

    if request.user.is_authenticated:
        return redirect(reverse('my-bookings', kwargs={'id': request.user.id}))
    else:
        reservation = Reservation.objects.filter(id=id)[0]
        return render(request, 'main/comfirm.html', {'reservation': reservation})


 # room_filters = Q()
                # room_filters &= Q(
                #             reservation__check_in_date__lte=check_out_date) 
                # room_filters &= Q(reservation__check_out_date__gte=check_in_date)
                # room_filters &= Q(reservation__reservation_status__in=excluded_statuses)
                             
                
                # if adults_count:
                #     room_filters &= Q(max_adults__gte=adults_count) 
                # if children_count:
                #     room_filters &= Q(max_children__gte=children_count)
               

                # # Exclude rooms that are booked for the specified date range

                # available_rooms = Room.objects.filter(room_filters
                  
                # ).distinct()