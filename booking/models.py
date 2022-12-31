from django.db import models
from cloudinary.models import CloudinaryField
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
from django.utils.html import escape
import datetime

class SessionType(models.Model):
    """
    Model for Admin Created Session Types.
    """
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    short_description = models.CharField(max_length=200)
    image = CloudinaryField('image', default='placeholder')
    price = models.DecimalField(max_digits=20, decimal_places=2)
    length = models.IntegerField(verbose_name='Session lenght(min)'
                                                       ' with customer')
    listed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title}"


class BookedSession(models.Model):
    """
    Model for booking of sessions.
    """
    STAUTS = ((0, 'Requested'),(1, 'Approved'))
    TIMES = ((0, '08:00'), (1, '09:00'), (2, '10:00'), (3, '11:00'), (4, '12:00'), (5, '13:00'), (6, '14:00'), (7, '15:00'), (8, '16:00'))
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=True,
                             blank=True)
    f_name = models.CharField(max_length=50, null=True, blank=True)
    l_name = models.CharField(max_length=50, null=True, blank=True)
    phone = models.IntegerField(null=True, blank=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    date = models.DateField(default=datetime.date.today)
    time = models.IntegerField(choices=TIMES)
    created_on = models.DateTimeField(auto_now_add=True)
    session_type = models.ForeignKey(
        SessionType, on_delete=models.PROTECT,
        related_name='session_type',
        null=True)
    status = models.IntegerField(choices=STAUTS, default=0)

    
class HeroImage(models.Model):
    """
    Model for setting the hero image slides
    """
    image = CloudinaryField('Image (16:9)', default='placeholder_cover')
    listed = models.BooleanField(default=False)
    SLIDE_NR_CHOICES = (
        (0,'First'),
        (1,'Second'),
        (2,'Third'),
        (3,'Fourth'),
        (4,'Fifth'),
    )
    slide_nr = models.IntegerField(choices=SLIDE_NR_CHOICES,)

    def __str__(self):
        return f"{self.slide_nr}"

