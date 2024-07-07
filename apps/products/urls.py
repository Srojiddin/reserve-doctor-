from django.urls import path

from .views import MedicineListView, MedicineCreateView,MedicineSingleListView, CartListView

urlpatterns = [
    path('shop/', MedicineListView.as_view(), name='shop'),
    path('medicine/create/', MedicineCreateView.as_view(), name='medicine_create'),
    path('medicine/single/', MedicineSingleListView.as_view(), name='product-single'),
    path('cart/', CartListView.as_view(), name='cart'),



]