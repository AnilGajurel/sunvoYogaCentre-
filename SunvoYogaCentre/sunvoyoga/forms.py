from django import forms
from sunvoyoga.models import User,Customer,Booking


class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields="__all__"


class CustomerForm(forms.ModelForm):
    class Meta:
        model=Customer
        fields="__all__"

class BookingForm(forms.ModelForm):
    class Meta:
        model=Booking
        fields="__all__"