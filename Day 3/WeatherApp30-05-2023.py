import requests
def getWeather():
    try:
        city=str(input("Enter your City: "))
        
    #weather
        api="https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=646824f2b7b86caffec1d0b16ea77f79"

        json_data = requests.get(api).json() 
        condition = json_data['weather'][0]['main'] 
        temp = int(json_data['main']['temp']-273.15)
        
        pressure = json_data['main']['pressure'] 
        humidity = json_data['main']['humidity']
        wind = json_data['wind']['speed']
        
        print("The Temperature of City is: ",temp,"°C") 
        print(condition, "|","FEELS", "LIKE", temp, "°C")
        print("Wind Speed is", wind)
        print("Humidity in Air is",humidity)
        print("Pressure of Atmosphere is",pressure)

    except :

        print("Weather App", "Invalid |")

getWeather()