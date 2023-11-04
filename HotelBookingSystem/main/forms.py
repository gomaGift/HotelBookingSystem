from django import forms
from . import models


class RoomForm(forms.ModelForm):
    class Meta:
        model = models.Room
        fields = ['room_type']

class RatingForm(forms.ModelForm):
    class Meta:
        model = models.Review
        fields = ['rating', 'comment']

class RoomFilterForm(forms.Form):
    features = forms.MultipleChoiceField(
        required=False, 
        widget=forms.CheckboxSelectMultiple, 
        choices = models.Feature.objects.values_list('id', 'name')
    )
    adults_count = forms.IntegerField(required=False, min_value=0)
    children_count = forms.IntegerField(required=False, min_value=0)
    bed_count = forms.IntegerField(required=False, min_value=0)

class AvailabilityCheckForm(forms.Form):
    check_in_date = forms.DateField()
    check_out_date = forms.DateField()
    adults_count = forms.IntegerField(required=False, min_value=0)
    children_count = forms.IntegerField(required=False, min_value=0)
       
class ReservationForm(forms.ModelForm):
    class Meta:
        model = models.Reservation
        fields = ['first_name', 'last_name', 'phone_number', 'email', 'check_in_date', 'check_out_date' ]

        
    check_in_date = forms.DateField(
        label='Check-In Date',
        widget=forms.DateInput(attrs={'class': 'form-control ','type': 'date'}),
    )
    check_out_date = forms.DateField(
        label='Check-Out Date',
        widget=forms.DateInput(attrs={'class': 'form-control ','type': 'date'}),
    )

class FindReservationForm(forms.Form):
    phone_email = forms.CharField(max_length=100, label='Phone or Email')
    reservation_id = forms.CharField(max_length=20)
    
