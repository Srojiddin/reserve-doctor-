from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from apps.products.models import  Medicine

from .forms import MedicineCreateForm


class MedicineCreateView(generic.CreateView):
    model = Medicine
    form_class = MedicineCreateForm
    template_name = 'medicine/medicine_create.html'
    success_url = reverse_lazy('shop')
    context_object_name = "products"


class MedicineListView(generic.ListView):
    model = Medicine
    template_name = 'shop.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = MedicineCreateForm()
        return context


class MedicineSingleListView(generic.ListView):
    model = Medicine
    template_name = 'shop-single.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = MedicineCreateForm()
        return context


class CartListView(generic.ListView):
    model = Medicine
    template_name = 'shopping-cart.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = MedicineCreateForm()
        return context
