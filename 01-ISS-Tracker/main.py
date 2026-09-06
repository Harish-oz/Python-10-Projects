import requests

# ISS API
url = "http://api.open-notify.org/iss-now.json"

# Get data from API
response = requests.get(url)

# Convert response to JSON
data = response.json()

# Get ISS location
latitude = data["iss_position"]["latitude"]
longitude = data["iss_position"]["longitude"]

# Display information
print("===== ISS TRACKER =====")
print("ISS Current Location")
print("----------------------")
print("Latitude :", latitude)
print("Longitude:", longitude)
print("======================")