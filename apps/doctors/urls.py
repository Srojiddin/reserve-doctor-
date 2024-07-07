from django.urls import path
from . import views

from apps.doctors.views import DoctorCreateView, DoctorListView, DoctorDetailView, DoctorUpdateView, DoctorDeleteView


urlpatterns = [
    path('doctor/create/', DoctorCreateView.as_view(), name='doctor_create'),
    path('doctor/', DoctorListView.as_view(), name='doctors_list'),
    path('doctor/<int:pk>/', DoctorDetailView.as_view(), name='doctor-detail'),
    path('doctor/update/<int:pk>/', DoctorUpdateView.as_view(), name='doctor_update'),
    path('doctors/<int:pk>/delete/', DoctorDeleteView.as_view(), name='doctor_delete'),
#     path('profile/view/', views.view_profile, name='view_profile'),
#     path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('cardiologist/', views.cardiologist_view, name='cardiologist'),
    path('gynaecologist/', views.gynaecologist_view, name='gynaecologist'),
    path('neurologist/', views.neurologist_list, name='neurologist-list'),
    path('ophthalmologist/', views.ophthalmologist_list, name='ophthalmologist-list'),
    path('aediatrician-/', views.paediatrician_list, name='paediatrician-list'),
    path('practitioner/', views.practitioner_list, name='practitioner-list'),




]


