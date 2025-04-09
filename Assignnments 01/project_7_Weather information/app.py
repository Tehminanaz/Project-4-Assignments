# Importing the 'requests' library to make HTTP requests to web APIs
import requests

# Importing 'pprint' to print the output in a neat and readable format
from pprint import pprint

# Store your API key (replace 'WEATHER_API' with your actual API key)
API_Key = 'WEATHER_API'

# Ask the user to enter the name of their city
city = input("Enter your city name: ")

# Create the full API URL using the base URL, API key, and the city name
base_url = "http://api.openweathermap.org/data/2.5/weather?appid=" + API_Key + "&q=" + city

# Send a request to the weather API and store the JSON response
weather_data = requests.get(base_url).json()

# Print the weather data in a clear and organized way
pprint(weather_data)
