import requests 

def get_bitcoin_price():
    # ۱. تنظیمات درخواست
    api_url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
    
    # ۲. دریافت داده از سرور
    response = requests.get(api_url)
    response.raise_for_status() # بررسی اینکه آیا اتصال موفق بود یا خیر
    
    # ۳. تبدیل پاسخ به فرمت قابل فهم (دیکشنری)
    data = response.json()
    
    # ۴. استخراج قیمت
    price_usd = data["bitcoin"]["usd"]
    price_toman = price_usd * 230000
    
    # ۵. نمایش خروجی
    print(f"Bitcoin price in USD: {price_usd}")
    print(f"Bitcoin price in Toman: {price_toman}")

# اجرای تابع
get_bitcoin_price()
