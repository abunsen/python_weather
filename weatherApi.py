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

    @property
    def temp_in_f(self):
        return str(pytemperature.k2f(self.weather['main']['temp'])
    
    @property
    def wind_speed(self):
        w = self.weather['wind']
        wind_speed = w['speed']
        return str(wind_speed)
                          
    def report(self):
        self.response = requests.get(self.complete_url)
        self.weather = self.response.json()
        # print(self.weather)
        if self.weather['cod'] != '404':
            city = self.weather['name']
            main = self.weather['main']
            hummidity = main['humidity']
            description = self.weather['weather'][0]['description']
            report = 'The temperature in ' + city + ' is ' + self.temp_in_f + ' with a windspeed of ' + self.wind_speed + ', ' + description + ' likely.'
         else:
            report = ""
         return report

city = input('Enter City Name: ')
w = Weather(city)
print w.report()

