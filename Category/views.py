from django.shortcuts import render
from .utils import crytocurrencyUtil
# Create your views here.
    
def index(request):
    if request.method == "GET":
        crytocurrencyUtil.updateCoins()
        coinlist = crytocurrencyUtil.coins       
    return render(request, 'index.html', {'coins': coinlist})