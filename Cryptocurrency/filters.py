
from cProfile import label
import django_filters
from .models import Coin

class CryptoFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(label= 'Nombre',lookup_expr='icontains')
    price = django_filters.CharFilter(label= 'Precio',lookup_expr='icontains')
    percent_change_24h = django_filters.CharFilter(label= '% Cambio 24h',lookup_expr='icontains')
   
    class Meta:
       model = Coin
       fields = ['name','price','percent_change_24h']