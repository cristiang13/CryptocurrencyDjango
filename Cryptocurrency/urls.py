
from django.urls import path
from . import views


urlpatterns = [
    path('save', views.save, name='save'),
    path('', views.getAllCryptocurrency, name='index'),
    path('favorite/<id>', views.favorite, name='favorite'),
    path('getFavorites', views.getCrytocurrencyFavorite, name='getFavorites'),
    path('deletefavorite/<id>', views.deleteFavorite, name='deletefavorite'),
    path('filters', views.filterCrypto, name='filters'),
    path('getCoin/<id>', views.getCoin, name='getCoin'),

   
]