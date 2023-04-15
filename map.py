import requests

# Replace with your own API key
API_KEY = "AIzaSyBtOmYvoGn5sY9foYWVIgDmd5abKEbVTs4"

# Set the addresses
origin = "New York, NY"
destination = "Los Angeles, CA"

# Send a request to the Google Maps Directions API
url = f"https://maps.googleapis.com/maps/api/distancematrix/json?origin={origin}&destination={destination}&key={API_KEY}"
response = requests.get(url)
data = response.json()
print(data)
# Extract the travel time
duration_in_traffic = data["routes"][0]["legs"][0]["duration_in_traffic"]["text"]
print(f"The travel time between {origin} and {destination} is {duration_in_traffic}.")
