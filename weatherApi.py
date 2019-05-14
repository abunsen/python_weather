import pytemperature
import requests,json

api_key = "d4fc50cffcc26b21c01a844564115245"
base_url = "https://api.openweathermap.org/data/2.5/weather?"

city = input('Enter City Name: ')
complete_url = base_url + "appid=" + api_key + "&q=" + city
response = requests.get(complete_url)
weather = response.json()

if weather['cod'] != '404':
    main = weather['main']

    hummidity = main['humidity']
    tempKelvin= main['temp']
    temperature = pytemperature.k2f(tempKelvin)
    temp = str(temperature)

    w = weather['wind']
    windSpeed = w['speed']
    
    wind = str(windSpeed)

    city = weather['name']

    description = weather['weather'][0]['description']
   

    print(description)

    report = 'The temperature in ' + city + ' is ' + temp + ' with a windspeed of ' + wind + ', ' + description + ' likely.'

    print(report)