from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import ListView, FormView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from apps.cart.models import Cart, Item, Favorite
from apps.cart.forms import AddToFavoriteForm


class CartDetailView(LoginRequiredMixin, ListView):
    template_name = 'shopping-cart.html'
    context_object_name = 'cart'

    def get_queryset(self):
        return get_object_or_404(Cart, user=self.request.user)


class MinusQuantityView(LoginRequiredMixin, View):

    def post(self, request, pk):
        item = get_object_or_404(Item, id=pk)
        if item.quantity - 1 == 0:
            item.delete()
        else:
            item.quantity -= 1
            item.save()
        return redirect('cart')


class PlusQuantityView(LoginRequiredMixin, View):

    def post(self, request, pk):
        item = get_object_or_404(Item, id=pk)
        item.quantity += 1
        item.save()
        return redirect('cart')


class AddToFavoriteView(LoginRequiredMixin, FormView):
    template_name = 'add_to_favorite.html'
    form_class = AddToFavoriteForm

    def form_valid(self, form):
        favorite = form.save(commit=False)
        favorite.user = self.request.user
        favorite.product_id = self.kwargs['product_id']
        favorite.save()
        return redirect('product_detail', product_id=self.kwargs['product_id'])


class RemoveFromFavoriteView(LoginRequiredMixin, View):

    def post(self, request, favorite_id):
        favorite = get_object_or_404(Favorite, id=favorite_id)
        favorite.delete()
        return redirect('favorites_list')
