#WEATHER APP USING TKINTER PYTHON
#INSTALL REQUIRED LIBRARIES USING PIP[TKINTER,REQUESTS]
#GET API KEY FROM OPENWEATHER.COM AND REPLACE IT IN PROGRAM
#PYTHON PROGRAM

import requests
import tkinter as tk
from tkinter import messagebox

def get_weather(api_key, city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)
    data = response.json()

    if data["cod"] != "404":
        temperature = data["main"]["temp"]
        weather_description = data["weather"][0]["description"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]

        result = f"Weather in {city}:\n"
        result += f"Temperature: {temperature} K\n"
        result += f"Description: {weather_description}\n"
        result += f"Humidity: {humidity}%\n"
        result += f"Wind Speed: {wind_speed} m/s"

        messagebox.showinfo("Weather Information", result)
    else:
        messagebox.showerror("Error", "City not found.")

def get_weather_button_click():
    city = city_entry.get()
    get_weather(api_key_entry.get(), city)

# Create the main window
window = tk.Tk()
window.title("Weather App")

# Create labels and entry fields for API key and city
api_key_label = tk.Label(window, text="API Key:")
api_key_label.pack()

api_key_entry = tk.Entry(window, width=30)
api_key_entry.pack()

city_label = tk.Label(window, text="City:")
city_label.pack()

city_entry = tk.Entry(window, width=30)
city_entry.pack()

# Create a button to get weather information
get_weather_button = tk.Button(window, text="Get Weather", command=get_weather_button_click)
get_weather_button.pack()

# Start the GUI event loop
window.mainloop()
