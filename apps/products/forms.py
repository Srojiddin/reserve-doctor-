from django import forms
from .models import Medicine


class MedicineCreateForm(forms.ModelForm):
    class Meta:
        model = Medicine
        fields = ['name', 'image_for_medicine', 'price_for_medicine',]