# Weather App using 3rd-party API- PY_learn projectn
## Import the requests module for HTTP requests
import requests

## Function to retrieve weather 
def fetch_weather(apiKey, city, measure='metric'):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={apiKey}&units={measure}"
    ### Error handling
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print('Request was successful :)')
            weatherData = response.json()

            ### Retrieve Temperature, Humidity and Conditions
            temperature = weatherData['main']['temp']
            if measure == 'metric': 
                sym = '°C' 
            else: 
                sym = '°F'
            humidity = weatherData['main']['humidity']
            condition = weatherData['weather'][0]['description']
            
            ### Display weather in city
            print(f'The current weather outlook for {city}:')
            print(f'Temperature: {temperature} {sym}')
            print(f'Humidity: {humidity}')
            print(f'Condition: {condition}')
        else:
            print(f"Error: {weatherData.get('cod')}")
            print(f'{weatherData.get('message', 'Unknown error')}')
    except requests.exceptions.RequestException as e:
        print(f'An error has occurred {e}')  
        
## Main program fuction
if __name__ == '__main__':
    apiKey = '______________________'
    cities = ['Paris', 'Tokyo', 'Sydney', 'London']
    fetch_weather(apiKey,'Pretoria')
    fetch_weather(apiKey,'New York','imperial')               
    fetch_weather(apiKey,cities[0])  
    fetch_weather(apiKey,cities[1])  
    fetch_weather(apiKey,cities[2],'imperial')     
    fetch_weather(apiKey,cities[3],'imperial')           
    
