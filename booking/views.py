from django.shortcuts import render
from django.views import View
from .models import *
from django.http import HttpResponseRedirect
from .forms import BookingForm
from datetime import datetime, timedelta
import json

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
        user_reg = {}
        yesterday = datetime.today() - timedelta(days=1)
        bookedQueryset = list(BookedSession.objects.filter(
                              booked_time__gt=yesterday).order_by(
                              "booked_time").values())
        schedulingQueryset = list(Scheduling.objects.filter(
                                 listed=True).order_by(
                                "title").values())
    
        for dict in bookedQueryset:
            dict["booked_time"] = dict["booked_time"].isoformat()
            dict["length"] = int(SessionType.objects.get(id=dict[
                'session_type_id']).customer_length)

        context = {
            "booked_sessions": json.dumps(bookedQueryset),
            "scheduling": json.dumps(schedulingQueryset),
            "booking_form": BookingForm()
            }
        return render(request, "booking.html", context=context)
