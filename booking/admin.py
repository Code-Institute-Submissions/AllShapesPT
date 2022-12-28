from django.contrib import admin
from .models import *
from datetime import timedelta


@admin.register(SessionType)
class SessionTypeAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'customer_length', 'real_length',
                    'listed')
    list_filter = ('title', 'price', 'customer_length', 'real_length',
                   'listed')
    search_fields = ['title', 'description', 'short_description',
                     'listed',]


@admin.register(Scheduling)
class SchedulingAdmin(admin.ModelAdmin):
    list_display = ['title']

@admin.register(BookedSession)
class BookedSessionAdmin(admin.ModelAdmin):
    list_display = ['booked_time', 'get_session_end', 'f_name', 'l_name',
                    'email', 'phone']
    search_fields = ['f_name', 'l_name', 'email', 'phone']

    def get_session_end(self, obj):
        length = int(obj.session_type.lenght)
        session_start = obj.booked_time
        session_end = session_start + timedelta(minutes=length)
        return session_end
