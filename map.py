import requests

# Replace with your own API key
API_KEY = "AIzaSyBtOmYvoGn5sY9foYWVIgDmd5abKEbVTs4"



def getTravelTime(origin, destination):
    # Send a request to the Google Maps Directions API
    url = f"https://maps.googleapis.com/maps/api/distancematrix/json?origins={origin}&destinations={destination}&key={API_KEY}"
    response = requests.get(url)
    data = response.json()
    # Extract the travel time
    return data["rows"][0]["elements"][0]["duration"]["value"]
    #print(f"The travel time between {origin} and {destination} is {duration_in_traffic}.")