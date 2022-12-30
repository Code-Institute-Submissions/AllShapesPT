from . import views
from django.urls import path

urlpatterns = [
    path('', views.view_items, name='home'),
    path('book', views.BookingView.as_view(), name="booking"),
]
