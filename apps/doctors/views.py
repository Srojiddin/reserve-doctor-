from collections import defaultdict
# from django.template.defaultfilters import slugify

from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from django.views import View

from apps.blogs.models import Blog
from apps.doctors.models import Doctor
from apps.doctors.forms import DoctorCreateForm, DoctorUpdateForm, DoctorDeleteForm

from django.contrib.auth.decorators import login_required
# from .models import DoctorProfile
# from .forms import DoctorProfileForm



class DoctorCreateView(generic.CreateView):
    model = Doctor
    form_class = DoctorCreateForm
    template_name = 'doctors/doctor_create.html'
    success_url = reverse_lazy('doctors_list')
    # context_object_name = "doctors.html"



class DoctorListView(generic.ListView):
    model = Doctor
    template_name = 'doctors.html'
    context_object_name = "doctors"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        grouped_doctors = defaultdict(list)
        for doctor in Doctor.objects.select_related('choosing_a_specialization').all():
            grouped_doctors[doctor.choosing_a_specialization.name].append(doctor)
        context['grouped_doctors'] = dict(grouped_doctors)  # Преобразуем defaultdict в обычный словарь
        return context


# class DoctorListView(generic.ListView):
#     model = Doctor
#     template_name = 'doctors.html'
#     context_object_name = "doctors"
#
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['form'] = DoctorCreateForm()
#         context['posts'] = Blog.objects.all()
#         return context


class DoctorDetailView(generic.DetailView):
    model = Doctor
    template_name = 'doctors-detail.html'
    context_object_name = 'doctors'
    pk_url_kwarg = 'pk'

    def doctor_detail(request, pk):
        doctor = get_object_or_404(Doctor, pk=pk)
        return render(request, 'doctor_detail.html', {'doctor': doctor})


class DoctorUpdateView(generic.UpdateView):
    model = Doctor
    form_class = DoctorUpdateForm
    template_name = 'doctors/doctor_update.html'
    success_url = 'doctors.html'


class DoctorDeleteView(generic.DeleteView):
    model = Doctor
    template_name = 'doctors/doctor_delete.html'
    context_object_name = 'doctor'
    success_url = reverse_lazy('doctors_list')
#
#
# @login_required
# def view_profile(request):
#     profile = request.user.doctor_profile
#     return render(request, 'profile/view_profile.html', {'profile': profile})
#
# @login_required
# def edit_profile(request):
#     profile = request.user.doctor_profile
#     if request.method == 'POST':
#         form = DoctorProfileForm(request.POST, instance=profile)
#         if form.is_valid():
#             form.save()
#             return redirect('view_profile')
#     else:
#         form = DoctorProfileForm(instance=profile)
#     return render(request, 'profile/edit_profile.html', {'form': form})