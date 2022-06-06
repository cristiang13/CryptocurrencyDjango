import json
from socket import timeout
from requests import  Session

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
  'start':'1',
  'limit':'20',
  'convert':'USD'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': '0b768e00-0e52-4ea9-93fd-ff1cbbd9f733',
}


session = Session()
session.headers.update(headers)


response = session.get(url, params=parameters)
data = json.loads(response.text)
#print(data)
coins=data['data']

def updateCoins():
    for coin in coins:
        price = coin['quote']['USD']['price'] 
        if (price <= 1):
            coin['quote']['USD']['price'] = round(coin['quote']['USD']['price'], 4)
            coin['quote']['USD']['percent_change_24h'] = round(coin['quote']['USD']['percent_change_24h'], 4)
        else:
            coin['quote']['USD']['price'] = round(coin['quote']['USD']['price'], 2)
            coin['quote']['USD']['percent_change_24h'] = round(coin['quote']['USD']['percent_change_24h'], 3)
        


# Grabs price based off of ticker
def getPrice(ticker):
    for coin in coins:
        if coin['symbol'] == ticker.upper():
            return coin['quote']['USD']['price']
    print("Invalid Ticker")
print(data)
