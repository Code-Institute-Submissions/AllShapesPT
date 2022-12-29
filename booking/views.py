from django.shortcuts import render
from django.views import View
from .models import *


class HomePage(View):
    
    def get(self, request):
        """
        Function to retrieve and display all session types created in admin.
        """

        queryset = list(SessionType.objects.filter(listed=True))
        sessiontypes = {"sessiontypes": queryset, "is_home": True}
        return render(request, "index.html", context=sessiontypes)
