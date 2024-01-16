import tkinter as tk
import requests

# Function about weather API
def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}q={city}&appid={api_key}&units=metric"

    response = requests.get(complete_url)

    if response.status_code == 200:
        weather_data = response.json()
        weather_info = f"Weather in {city}:\n" \
                       f"Description: {weather_data['weather'][0]['description']}\n" \
                       f"Temperature: {weather_data['main']['temp']}°C\n" \
                       f"Humidity: {weather_data['main']['humidity']}%\n" \
                       f"Wind Speed: {weather_data['wind']['speed']} m/s"
        return weather_info
    else:
        return "Failed to fetch weather data."


# Variable container which will store an OpenWeatherMap API key. (this string is empty but you can put in an API key from the website)
api_key = ''

# Function about UI window
def UI_window():
    def on_button_click():
        city = city_entry.get()  # Get the city name from the entry field
        weather_info = get_weather(api_key, city)
        print(weather_info)

        weather_window = tk.Tk()
        weather_window.title("Weather Information")
        weather_window.geometry("300x150")

        weather_label = tk.Label(weather_window, text=weather_info, padx=10, pady=10)
        weather_label.pack()

        weather_window.mainloop()

    root = tk.Tk()
    root.title("Weather App")
    root.geometry("300x150")

    label = tk.Label(root, text="Enter city name:")
    label.pack()

    city_entry = tk.Entry(root)
    city_entry.pack()

    button = tk.Button(root, text="Get Weather", command=on_button_click)
    button.pack()

    root.mainloop()


if __name__ == "__main__":
    UI_window()
