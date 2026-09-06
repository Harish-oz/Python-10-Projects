import requests

movie = input("Enter movie name: ")

url = f"https://www.omdbapi.com/?t={movie}&apikey=c524a850"

response = requests.get(url)
data = response.json()

print("\n===== MOVIE FINDER =====")

if data["Response"] == "True":
    print("Title       :", data["Title"])
    print("Year        :", data["Year"])
    print("Genre       :", data["Genre"])
    print("IMDb Rating :", data["imdbRating"])
    print("Director    :", data["Director"])
    print("Actors      :", data["Actors"])
    print("Plot        :", data["Plot"])
else:
    print("Movie not found.")

print("========================")