import requests

url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd,eur"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    usd_price = data['bitcoin']['usd']
    eur_price = data['bitcoin']['eur']
    toman_price = usd_price * 230000
    print('============')
    print('respons bit price')
    print(f'price in usd:${usd_price:,2f}')
    print(f'price in eur:€{eur_price:,2f}')
    print(f'price in irr:{toman_price:,} Toman')
    print('============')
else:
    print("Error connecting to server")
