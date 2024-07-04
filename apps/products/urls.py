from django.urls import path

from .views import MedicineListView, MedicineCreateView

urlpatterns = [
    path('shop/', MedicineListView.as_view(), name='shop'),
    path('medicine/create/', MedicineCreateView.as_view(), name='medicine_create'),

]