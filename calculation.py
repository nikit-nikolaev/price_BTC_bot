import requests

def price_BTC_usd():
    url = 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd'
    response = requests.get(url)
    data = response.json()
    price = f"{(data['bitcoin']['usd']):,d}"
    return (price)

print(price_BTC_usd())

def price_BTC_rub():
    url = 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=rub'
    response = requests.get(url)
    data = response.json()
    price = f"{(data['bitcoin']['rub']):,d}"
    return (price)

print(price_BTC_rub())
