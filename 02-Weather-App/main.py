import requests

city = input("Enter city name: ")

url = f"https://wttr.in/{city}?format=j1"

response = requests.get(url)
data = response.json()

current = data["current_condition"][0]

temperature = current["temp_C"]
humidity = current["humidity"]
wind = current["windspeedKmph"]
condition = current["weatherDesc"][0]["value"]

print("\n===== WEATHER APP =====")
print("City      :", city)
print("Condition :", condition)
print("Temperature:", temperature, "°C")
print("Humidity  :", humidity, "%")
print("Wind Speed:", wind, "km/h")
print("=======================")