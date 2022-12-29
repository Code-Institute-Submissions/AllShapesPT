from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.view_items, name='home'),
]
