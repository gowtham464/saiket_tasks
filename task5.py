import requests

def currency_convert(amount,from_currency,to_currency):
    try:
        url=f"https://v6.exchangerate-api.com/v6/4f10e0c5d19a25cf1bd846c7/latest/{from_currency}"
        Permission=requests.get(url)
        if Permission.status_code==200:
            data=Permission.json()
            rates=data["conversion_rates"]
            if to_currency in rates:
                rate=rates[to_currency]
                convert=amount*rate
                return convert
            else:
                return f"currency {to_currency} not supported"
        else:
            return "not fetched"
    except Exception as e:
        print(e)
        
amount=float(input("enter a amount: "))
from_currency=input("enter a from_currency: ").upper()
to_currency=input("enter a to_currency: ").upper()
result=currency_convert(amount,from_currency,to_currency)
print(f"{amount}{from_currency} - {result} {to_currency}")