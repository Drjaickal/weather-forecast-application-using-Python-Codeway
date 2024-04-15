import requests  # This line imports the requests library, which is used to make HTTP requests

api_key = "4365f010c97daf6170edb93ebbe97589"  # This line stores your OpenWeatherMap API key in a variable

userinput = input("enter the city name: ")  # This line prompts the user to enter a city name and stores it in a variable

weatherdata = requests.get(  # This line makes a GET request to the OpenWeatherMap API
    f"https://api.openweathermap.org/data/2.5/weather?q={userinput}&units=imperial&APPID={api_key}"  # This line constructs the URL for the API request, including the user-entered city name, your API key, and units set to imperial
)

weather = weatherdata.json()['weather'][0]['main']  # This line extracts the weather condition from the JSON response
temp = round(weatherdata.json()['main']['temp'])  # This line extracts the temperature in Kelvin from the JSON response and rounds it
hum = round(weatherdata.json()['main']['humidity'])  # This line extracts the humidity from the JSON response and rounds it

print(f"the weather in {userinput} is: {weather}")  # This line prints the weather condition for the entered city
print(f"the temperature in {userinput} is: {temp} degrees Fahrenheit")  # This line prints the temperature in Fahrenheit for the entered city
print(f"the humidity in {userinput} is: {hum} percent")  # This line prints the humidity for the entered city
