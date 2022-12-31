from .models import SessionType, BookedSession
from django import forms
from datetime import datetime
from collections import defaultdict


class BookingForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(BookingForm, self).__init__(*args, **kwargs)
        session_types = SessionType.objects.filter(listed=True).order_by("title").values()
        session_dropdown = [(str(
            i["id"]) + "," + str(
                i["length"]), i["title"] + " - " + str(
                    i["length"]) + " min - ₩" + str(i["price"])) for i in session_types]


        self.fields['title'] = forms.ChoiceField(choices=session_dropdown)
        self.fields['title'].required = True
        self.fields['title'].label = 'Session Type'
        self.fields['date'] = forms.CharField()
        self.fields['date'].required = True
        self.fields['date'] = forms.DateField(widget=forms.DateInput(format='%Y-%m-%d'))
        self.field['time'].label = Time
        self.field['time'].required=True
        self.fields['email'].required = True
        self.fields['f_name'].required = True
        self.fields['f_name'].label = "First Name"
        self.fields['l_name'].required = True
        self.fields['l_name'].label = "Last Name"
        self.fields['phone'].required = True
        self.fields['phone'].label = "Phone Number"
        for fieldname, field in self.fields.items():
            field.widget.attrs.update({'class': 'custom-form-field'})
        
    class Meta:
        model = BookedSession
        fields = (
            'email',
            'f_name',
            'l_name',
            'date',
            'time',
            'phone',)
    