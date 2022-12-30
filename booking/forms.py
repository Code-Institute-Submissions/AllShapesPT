from .models import SessionType, BookedSession
from django import forms
from datetime import datetime

class BookingForm(forms.ModelForm):
    class Meta:
        model = BookedSession
        fields = (
            'email',
            'f_name',
            'l_name',
            'booked_time',
            'session_type',
            'phone',)
        labels = {
            'email': 'Email Adress',
            'f_name': 'First Name',
            'l_name': 'Last Name',
            'booked_time': 'Time & Date',
            'phone': 'Phone Number',
        }

    def __init__(self, *args, **kwargs):
        super(BookingForm, self).__init__(*args, **kwargs)
        session_types = SessionType.objects.filter(listed=True).order_by("title").values()
        session_dropdown = [(str(
            i["id"]) + "," + str(
                i["customer_length"]), i["title"] + " - " + str(
                    i["customer_length"]) + " min - ₩" + str(i["price"])) for i in session_types]
        self.fields['title'] = forms.ChoiceField(choices=session_dropdown)
        self.fields['booked_time'].required = True
        self.fields['booked_time'] = forms.CharField()
        self.fields['booked_time'].widget.attrs.update({'id': 'datetimepicker'})
        self.fields['email'].required = True
        self.fields['f_name'].required = True
        self.fields['l_name'].required = True
        for fieldname, field in self.fields.items():
            field.widget.attrs.update({'class': 'custom-form-field'})
        