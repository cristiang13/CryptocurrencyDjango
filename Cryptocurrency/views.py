from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Coin
from Category.utils import crytocurrencyUtil
from django.contrib import messages
from .filters import CryptoFilter

# Create your views here.
def save(request):
    crytocurrencyUtil.updateCoins()
    coinlist = crytocurrencyUtil.coins
    for coin in coinlist:
        crypto = Coin.objects.create(
        name=coin['name'], price=coin['quote']['USD']['price'], percent_change_24h=coin['quote']['USD']['percent_change_24h'])
               
    messages.success(request, '¡Datos de la tabla guardados!')
    return redirect('index')

def getAllCryptocurrency(request):
    allsCryptocurrency = Coin.objects.all()
    return render(request, "getCryptocurrency.html", {"cryptocurrencys": allsCryptocurrency})

def favorite(request, id):
   coin = Coin.objects.get(id=id)
   coin.favorite = True
   coin.save()
   messages.success(request, '¡Coin agregado como favorito!')
   return redirect('getFavorites')
   #return HttpResponse(coin)

def getCrytocurrencyFavorite(request):
    allsCryptocurrency = Coin.objects.all()
    return render(request, "getFavoritesCrypto.html", {"cryptocurrencys": allsCryptocurrency})

def deleteFavorite(request,id):
    coin = Coin.objects.get(id=id)
    coin.favorite = False
    coin.save()
    messages.success(request, '¡Se elimino Coin: '+coin.name+' de favorito!')
    return redirect('getFavorites')


def filterCrypto(request):
    allsCryptocurrencys = Coin.objects.all()
    cryptofilter= CryptoFilter(request.GET,queryset=allsCryptocurrencys)
    allsCryptocurrencys=cryptofilter.qs
    context={'cryptocurrencys': allsCryptocurrencys ,'cryptofilter':CryptoFilter}
    return render(request, "filters.html", context)

def getCoin(request, id):
    coin = Coin.objects.get(id=id)
    return render(request, "detalle.html", {"coin": coin})