# Weather Application

This is a simple weather application that allows users to check the weather information for any city. It provides key weather details like temperature, humidity, pressure, wind speed, and description, with an extra notification based on the weather conditions (e.g., umbrella reminders, temperature warnings).

The application is built using Python and the OpenWeatherMap API. The front-end is interactive and uses `ipywidgets` for creating a user-friendly experience in a Jupyter Notebook environment.

## Features
- **City Input**: Allows the user to input a city name.
- **Weather Info**: Displays the weather information including temperature, humidity, wind speed, and pressure.
- **Weather Notifications**: Alerts users if the weather conditions are extreme, such as heavy rain or extreme temperatures.
- **Dynamic UI**: Stylish, responsive design with an interactive widget interface.

## Requirements

To run this project, you'll need the following Python libraries:

- `ipywidgets`: For creating the interactive widgets.
- `requests`: To fetch data from the OpenWeatherMap API.
- `IPython`: For displaying HTML in Jupyter notebooks.

You can install the required libraries using pip:

```bash
pip install ipywidgets requests ipython
```
## Setup
-**Get OpenWeatherMap API Key:**
To use this application, you'll need an API key from OpenWeatherMap. You can get one by signing up on their website.

-**Replace the API Key:**
Once you have the API key, replace the value of API_KEY in the code with your actual key:
```bash
API_KEY = "your_actual_api_key_here"
```
## Usage
-**Input a City:**
Enter the name of the city you'd like to check the weather for in the input field.

-**Get Weather:**
Click the "Get Weather" button to fetch the current weather data for the entered city.

-**View Results:**
The weather details will be displayed below the input field along with an icon representing the current weather. If the conditions are extreme, you'll receive a notification, such as an umbrella reminder for rain or a warning for hot or cold temperatures.

## Example
![image](https://github.com/user-attachments/assets/c26dad51-eca0-435d-91d3-08e3ec71c796)


**Additionally, if it's raining, a message will be displayed:**
-☔ Don't forget your umbrella!

