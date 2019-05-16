import pytemperature
import requests,json
import os

class Weather:
    api_key = os.environ.get('WEATHER_API')
    base_url = "https://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "appid=" + api_key + "&q=" 


    def __init__(self, location):
        self.complete_url = self.complete_url + location

    def showAPI(self):
        print(self.complete_url)

    def getRequest(self):
        self.response = requests.get(self.complete_url)
        self.weather = self.response.json()
        # print(self.weather)
        if self.weather['cod'] != '404':
            main = self.weather['main']
            hummidity = main['humidity']

            kelvin = main['temp']
            temperature = pytemperature.k2f(kelvin)
            temp = str(temperature)

            w = self.weather['wind']
            windSpeed = w['speed']
            wind = str(windSpeed)

            city = self.weather['name']
            description = self.weather['weather'][0]['description']

          
            report = 'The temperature in ' + city + ' is ' + temp + ' with a windspeed of ' + wind + ', ' + description + ' likely.'
            
            print(report)
            

city = input('Enter City Name: ')
w = Weather(city)
w.getRequest()

