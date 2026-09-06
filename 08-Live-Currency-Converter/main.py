import requests

amount = float(input("Enter amount: "))
from_currency = input("From currency (USD, EUR, INR): ").upper()
to_currency = input("To currency (USD, EUR, INR): ").upper()

url = f"https://open.er-api.com/v6/latest/{from_currency}"

response = requests.get(url)
data = response.json()

if response.status_code == 200 and data["result"] == "success":
    rate = data["rates"][to_currency]
    converted = amount * rate

    print("\n===== LIVE CURRENCY CONVERTER =====")
    print("Amount    :", amount, from_currency)
    print("Rate      :", rate)
    print("Converted :", round(converted, 2), to_currency)
    print("===================================")

else:
    print("Currency not found.")