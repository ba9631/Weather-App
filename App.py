#  Imports
import ipywidgets as widgets
from IPython.display import display, HTML
import requests

#  OpenWeatherMap API setup
API_KEY = "161450c5d7eb81b0302448eeb72b9383"  # Replace with your actual API key
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"

#  Widgets
city_input = widgets.Text(
    value='',
    placeholder='Enter city name',
    description='City:',
    layout=widgets.Layout(width='300px', height='40px'),
    style={'description_width': 'initial'}
)

fetch_button = widgets.Button(
    description="Get Weather",
    button_style="info",
    layout=widgets.Layout(width='200px', height='40px')
)

output = widgets.Output()

def show_weather(data):
    if data["cod"] == 200:
        main = data["main"]
        weather = data["weather"][0]
        temp = main["temp"]
        humidity = main["humidity"]
        pressure = main["pressure"]
        wind_speed = data["wind"]["speed"]
        description = weather["description"]
        icon = weather["icon"]
        city_name = data["name"]
        country = data["sys"]["country"]

        display(HTML(f"""
        <div style="
            background: linear-gradient(to right, #83a4d4, #b6fbff);
            border-radius: 15px;
            padding: 25px;
            box-shadow: 0 8px 16px rgba(0,0,0,0.15);
            width: 420px;
            margin: 20px auto;
            font-family: 'Arial', sans-serif;
            color: #003366;
        ">
            <h2 style="text-align: center; font-weight: bold;">Weather in {city_name}, {country}</h2>
            <div style="text-align: center;">
                <img src="http://openweathermap.org/img/wn/{icon}@2x.png" alt="weather-icon">
            </div>
            <ul style="list-style: none; padding-left: 0;">
                <li><b>🌡️ Temperature:</b> {temp}°C</li>
                <li><b>🌥️ Description:</b> {description.title()}</li>
                <li><b>💧 Humidity:</b> {humidity}%</li>
                <li><b>🌬️ Wind Speed:</b> {wind_speed} m/s</li>
                <li><b>📊 Pressure:</b> {pressure} hPa</li>
            </ul>
        </div>
        """))

        notify_user_about_weather(description.lower(), temp)
    else:
        display(HTML("<h3 style='color: red;'>❌ City not found. Try again.</h3>"))


# Notification logic
def notify_user_about_weather(description, temp):
    message = ""
    if "rain" in description or "storm" in description:
        message = "☔ Don't forget your umbrella!"
    elif "snow" in description:
        message = "❄️ It's snowy! Wear warm clothes."
    elif temp > 35:
        message = "🥵 It's hot outside. Stay hydrated!"
    elif temp < 5:
        message = "🥶 It's cold! Wear a jacket."

    if message:
        display(HTML(f"<h4 style='color: orange;'>{message}</h4>"))

# Button event
def get_weather_info(b):
    output.clear_output()
    city_name = city_input.value
    if not city_name:
        with output:
            display(HTML("<h3 style='color: red;'>Please enter a city name.</h3>"))
        return
    complete_url = f"{BASE_URL}appid={API_KEY}&q={city_name}&units=metric"
    response = requests.get(complete_url)
    data = response.json()

    with output:
        show_weather(data)

#  Linking button to function
fetch_button.on_click(get_weather_info)

# Displaying widgets
display(widgets.VBox([city_input, fetch_button, output]))
