## get the weather condition (rainy, cloudy) for any given city
## by @limitedmage julianapena.com

import urllib.request
import urllib.parse
import json

def get_weather(city, api_key):
    # Create the URL for the OpenWeatherMap API
    url = f"http://api.openweathermap.org/data/2.5/weather?q={urllib.parse.quote(city)}&appid={api_key}&units=metric"

    try:
        # Send a GET request to the API
        with urllib.request.urlopen(url) as response:
            # Read and decode the response
            data = response.read().decode('utf-8')
    except urllib.error.URLError as e:
        # If there was an error, return the error message
        return f"Error: {e.reason}"

    try:
        # Parse JSON response
        data_json = json.loads(data)

        # Check if the response contains the weather information
        if data_json.get('cod') != 200:
            return "Invalid city or error retrieving data"

        # Extract weather condition
        weather = data_json['weather'][0]['description']
        return f"Weather in {city}: {weather.capitalize()}"
    except (json.JSONDecodeError, KeyError) as e:
        return "Error parsing the weather data"

def main():
    # Your API key for OpenWeatherMap (sign up for a free key at https://openweathermap.org/)
    api_key = 'YOUR_API_KEY_HERE'
    
    city = input("Give me a city: ")
    print(get_weather(city, api_key))

if __name__ == "__main__":
    main() 