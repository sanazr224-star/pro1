import requests
url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd,eur"
def get_bit_price():
    try:
        respons=requests.get(url)
        if requests.status_codes == 200 :
            data = requests.json()
            usd_p = data['bitcoin']['usd']
            eur_p = data['bitcoin']['eur']
            toman_p = usd_p*230000
            print('============')
            print('respons bit price')
            print(f'price in usd:${usd_p:,2f}')
            print(f'price in eur:€{eur_p:,2f}')
            print(f'price in irr:{toman_price:,} Toman')
            print('============')
        else:
            print("Error not connect to the website: Could")
    except Exception as e:
        print(f"An error occurred:{e}")
if __name__ == "__main__":
   get_bit_price()

