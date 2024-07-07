from django import forms
from apps.appointments.models import Appointment


class AppointmentCreateForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['fullname', 'choosing_a_disease', 'choosing_a_doctor', 'date_of_reservation']

class AppointmentDetailForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = '__all__'


class AppointmentUpdateForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = '__all__'


class AppointmentDeleteForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = '__all__'




