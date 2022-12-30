from django.shortcuts import render
from django.views import View
from .models import *
from django.http import HttpResponseRedirect


# class HomePage(View):

    # def get(self, request):
    #     """
    #     Function to retrieve and display all session types created in admin.
    #     """
    #     queryset = list(SessionType.objects.filter(listed=True))
    #     sessiontypes = {"sessiontypes": queryset, "is_home": True}
    #     return render(request, "index.html", context=sessiontypes)

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

# class BookingView(View):
#      """
#     View for booking page
#     """
#     def get(self,request):
#         user_reg{}
#     yesterday = datetime.today() - timedelta(days=1)
#     bookedQueryset = list(BookedSession.objects.filter(
#         date_time__gt=yesterday).order_by("date_time").values())
#     planningQueryset = list(Planning.objects.filter(active=True).order_by("title").values())