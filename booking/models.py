from django.db import models
from cloudinary.models import CloudinaryField
from django.core.validators import RegexValidator
from django.contrib.auth.models import User


class Scheduling(models.Model):
    """
    Model for scheduling of bookable times.
    """
    title = models.CharField(
        max_length=100,
        unique=True, 
        default='Default Schedule',
    )

    days_off = models.CharField(
        max_length=10, 
        verbose_name='Weekly days off',
        validators=[RegexValidator(
            r'^[1-7](,[1-7])*$',
            message='Wrong format entered!'
            )],
        help_text='Weekdays = 1-7, 1 Being monday, 7 being sunday. Add '
                  'weekdays off, comma separated Example for Wednesdays &'
                  'Fridays off: 3,5'

    )

    special_days_off = models.TextField(
        verbose_name='Holidays and other special days off',
        validators=[RegexValidator(
            r'^(\s{0,})(\d{4}\-\d{2}\-\d{2})(,\d{4}\-\d{2}\-\d{2}){1,}(\s){0,}$',
            message='Wrong format entered!'
            )],
        help_text='Enter dates, comma separated, no space '
                  'Example: 2023-01-01,2023-12-31'
        
    )

    bookable_times = models.TextField(
        validators=[RegexValidator(
            r'^(?:[01]\d|2[1-3]):[0-5]\d(?::[0-5]\d)?'
            r'(?:,(?:[01]\d|2[1-3]):[0-5]\d(?::[0-5]\d)?)*$',
            message='Wrong format entered!'
            )],
        help_text='Format is HOURS:MINUTES, comma separated, no space, '
                  'Example: 08:15,10:30,11:00'
    )
    listed = models.BooleanField(default=False, verbose_name='Active schedule')


class SessionType(models.Model):
    """
    Model for Admin Created Session Types.
    """
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    short_description = models.CharField(max_length=200)
    image = CloudinaryField('image', default='placeholder')
    price = models.DecimalField(max_digits=20, decimal_places=2)
    customer_length = models.IntegerField(verbose_name='Session lenght(min)'
                                                       ' with customer')
    real_length = models.IntegerField(verbose_name='Session lenght(min)'
                                                   ' including prep/post work')
    listed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title}, {self.customer_length} Min, ₩{self.price}"


class BookedSession(models.Model):
    """
    Model for booking of sessions.
    """
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=True,
                             blank=True)
    f_name = models.CharField(max_length=50, null=True, blank=True)
    l_name = models.CharField(max_length=50, null=True, blank=True)
    phone = models.IntegerField(null=True, blank=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    booked_time = models.DateTimeField()
    created_on = models.DateTimeField(auto_now_add=True)
    session_type = models.ForeignKey(
        SessionType, on_delete=models.PROTECT,
        related_name='session_type',
        null=True)
    
    def confirm(self, *args, **kwargs):
        self.booked_time = self.booked_time.replace(tzinfo=None)
        super(BookedSession, self).save(*args, **kwargs)


