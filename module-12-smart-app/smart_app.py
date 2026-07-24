import urllib.request
import json

def main():
    while True:
        # 📌 Step 2: Program Introduction
        print("=" * 50)
        print("Welcome to Smart Text Analyzer & Live Data App")
        print("=" * 50)
        print()

        # 📌 Step 3: String Analyzer Section
        print("--- [Step 3: String Analyzer] ---")
        sentence = input("Enter a sentence: ").strip()
        
        # 📌 Step 7: Error Handling (Empty input check)
        if not sentence:
            print("Error: You entered an empty sentence. Skipping analysis.\n")
        else:
            total_chars = len(sentence)
            words = len(sentence.split())
            
            # Palindrome check (ignoring spaces and case)
            clean_sentence = "".join(sentence.split()).lower()
            is_palindrome = clean_sentence == clean_sentence[::-1]
            
            print(f"Total Characters (with spaces): {total_chars}")
            print(f"Word Count: {words}")
            print(f"Is Palindrome?: {'Yes' if is_palindrome else 'No'}")
            print()

        # 📌 Step 4: Sorting Logic Section
        print("--- [Step 4 & 5: Sorting & Algorithmic Thinking] ---")
        num_input = input("Enter a list of numbers (comma-separated, e.g., 5,2,9,1): ").strip()
        
        # 📌 Step 7: Error Handling (Empty and format check)
        if not num_input:
            print(" Error: No numbers entered.\n")
            return

        try:
            # Convert input into a list of floats/integers
            # 📌 Step 8 (Debugging Practice Fixed): Handled conversion explicitly
            numbers = [float(x.strip()) for x in num_input.split(",") if x.strip()]
            
            if not numbers:
                print("Error: Valid numbers could not be parsed.\n")
                return
                
        except ValueError:
            print("Error: Wrong number format! Please ensure you only enter numbers separated by commas.\n")
            return

        # Python built-in sorting for Step 4
        ascending_order = sorted(numbers)
        descending_order = sorted(numbers, reverse=True)
        
        print(f"Ascending Order: {ascending_order}")
        print(f"Descending Order: {descending_order}")

        # 📌 Step 5: Algorithm Thinking Challenge (Without max() or min())
        # Custom loop to find max and min
        largest = numbers[0]
        smallest = numbers[0]
        
        for num in numbers:
            if num > largest:
                largest = num
            if num < smallest:
                smallest = num
                
        print(f"Largest Number (Algorithmic): {largest}")
        print(f" Smallest Number (Algorithmic): {smallest}")
        print()

        # 📌 Step 6: API Integration (Mini App)
        print("--- [Step 6: Live Weather Data API] ---")
        print("Fetching live temperature for Dhaka, Bangladesh...")
        
        # Using free Open-Meteo API (No API key required) for Dhaka coordinates
        api_url = "https://api.open-meteo.com/v1/forecast?latitude=23.8103&longitude=90.4125&current_weather=true"
        
        try:
            # Fetching data using python's built-in urllib
            with urllib.request.urlopen(api_url, timeout=10) as response:
                if response.status == 200:
                    data = json.loads(response.read().decode())
                    current_weather = data.get("current_weather", {})
                    temperature = current_weather.get("temperature")
                    windspeed = current_weather.get("windspeed")
                    
                    print(f"Location: Dhaka")
                    print(f"Current Temperature: {temperature}°C")
                    print(f"Wind Speed: {windspeed} km/h")
                else:
                    print("Could not fetch data from the API server.")
        except Exception as e:
            print(f"API Error: Unable to fetch live data (Check internet connection). Details: {e}")
            
        print("\n" + "=" * 50)
        print("Thank you for using the Smart App!")
        print("=" * 50)
   
main()