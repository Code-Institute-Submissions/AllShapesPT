from django.contrib import admin
from .models import *
from datetime import timedelta


@admin.register(SessionType)
class SessionTypeAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'length',
                    'listed', )
    list_filter = ('title', 'price', 'length',
                   'listed')
    search_fields = ['title', 'description', 'short_description',
                     'listed',]


@admin.register(BookedSession)
class BookedSessionAdmin(admin.ModelAdmin):
    list_display = ('date', 'time', 'f_name', 'l_name',
                    'email', 'phone', 'created_on', 'status')
    search_fields = ['f_name', 'l_name', 'email', 'phone', 'status',]


@admin.register(HeroImage)
class HeroImageAdmin(admin.ModelAdmin):
    list_display = ('image', 'slide_nr', 'listed',)
    list_filter = ('image', 'slide_nr', 'listed',)