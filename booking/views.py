from django.shortcuts import render
from django.views import View, generic
from .models import *
from django.http import HttpResponseRedirect
from .forms import BookingForm
from datetime import datetime, timedelta
from bootstrap_datepicker_plus.widgets import DateTimePickerInput



def view_items(request):
    """
    Function to render homepage view
    """
    sessiontypes = SessionType.objects.filter(listed=True)
    heroimages = HeroImage.objects.filter(listed=True)
    context = {
        'sessiontypes': sessiontypes,
        'heroimages': heroimages
        }
    return render(request, 'index.html', context)


class BookingView(View):
    """
    View for booking page
    """


    def get(self, request):
        context = {
            "booking_form": BookingForm()
            }
        return render(request, "booking.html", context=context)