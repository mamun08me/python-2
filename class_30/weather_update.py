import requests

API_KEY = "073dc95d140e443f851150223260501"
BASE_URL = "http://api.weatherapi.com/v1"

def get_current_weather(city):
    endpoint = f"{BASE_URL}/current.json"
    params = {
        "key": API_KEY,
        "q": city
    }

    try:
        response = requests.get(endpoint, params=params)
        
        # Check if the API request was successful
        if response.status_code == 200:
            data = response.json()

            location = data["location"]["name"]
            country = data["location"]["country"]
            temp_c = data["current"]["temp_c"]
            condition = data["current"]["condition"]["text"]
            humidity = data["current"]["humidity"]
            feelslike_c = data["current"]["feelslike_c"]
            
            print(f"Weather in {location}, {country}:")
            print(f"Temperature: {temp_c}°C (Feels like: {feelslike_c}°C)")
            print(f"Condition: {condition}")
            print(f"Humidity: {humidity}%\n")
        else:
            print(f"Error: Could not find weather data for '{city}'. (Status Code: {response.status_code})\n")
            
    except requests.exceptions.RequestException as e:
        print(f"Network error occurred: {e}")

# --- EXECUTION ---
get_current_weather("Dhaka")
get_current_weather("Rajshahi")
get_current_weather("Chittagang")  # Fixed spelling from Chittagong to Chattogram
