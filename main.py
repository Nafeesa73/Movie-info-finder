

import requests


title = input("Enter a movie title: ")

api_key =  "bd8ac12e"
url = f"http://www.omdbapi.com/?t={title}&apikey={api_key}"

response = requests.get(url)
data = response.json()


if data.get("Response") == "True":
    print("Movie found!")
    print(f"Title: {data.get('Title')}")
    print(f"Year: {data.get('Year')}")
    print(f"Genre: {data.get('Genre')}")
    print(f"Director: {data.get('Director')}")
    print(f"Plot: {data.get('Plot')}")
    print(f"IMDb_rating: {data.get('Plot')}")
else:
    print("Movie not found or invalid API key.")
    print(f"Error message: {data.get('Error')}")






