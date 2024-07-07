from django.urls import path
from apps.cart.views import  MinusQuantityView, PlusQuantityView, AddToFavoriteView, RemoveFromFavoriteView

urlpatterns = [
    # path('cart/', CartDetailView.as_view(), name='cart'),
    path('minus/<int:pk>/', MinusQuantityView.as_view(), name='minus_quantity'),
    path('plus/<int:pk>/', PlusQuantityView.as_view(), name='plus_quantity'),
    path('product/<int:product_id>/add-to-favorite/', AddToFavoriteView.as_view(), name='add_to_favorite'),
    path('favorite/<int:favorite_id>/remove/', RemoveFromFavoriteView.as_view(), name='remove_from_favorite'),
]
