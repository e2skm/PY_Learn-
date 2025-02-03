# Create a simple HTTP Client - PY_Learn projectn
## Import the neccessary modules
import requests, json, random

## Function to prompt the user to select a website. 
def get_website_url():
    while True:
        try:
            print('Enter any of the following numbers to select a website:')
            print('1. https://jsonplaceholder.typicode.com/posts')
            print('2. https://reqres.in/api/users')
            choice = int(input('Your choice: '))
            if choice == 1:
                return 'https://jsonplaceholder.typicode.com/posts'
            elif choice == 2:
                return 'https://reqres.in/api/users'
            else:
                print('Invalid number entered. Please try again.')
        except ValueError:
            print('Invalid input. Please enter a number.')
            
### Function to get data in JSON format for both websites respectively
def get_json_data(websiteChoice):
    if websiteChoice == 1:
        return {"title": "foo", "body": "bar", "userId": 1}
    else:
        return {"name": "morpheus", "job": "leader"}            

## Function to prompt the user to select an HTTP method              
def get_http_method():
    while True:
        try:
            print('Enter any of the following numbers to select an HTTP method:')
            print('1. GET')
            print('2. POST')
            print('3. PUT')
            print('4. DELETE')
            choice = int(input('Your choice: '))
            if choice in [1, 2, 3, 4]:
                return choice
            else:
                print('Invalid number entered. Please try again.')
        except ValueError:
            print('Invalid input. Please enter a number.')
            

## Function to make an HTTP request and load the response                
def make_request(url, method, jsonData=None):
    
    try:
        if method == 1:
            response = requests.get(url)
        elif method == 2:
            response = requests.post(url, json=jsonData)
        elif method == 3:
            response = requests.put(url, json=jsonData)
        elif method == 4:
            response = requests.delete(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response
    except requests.exceptions.RequestException as e:
        print(f'An error occurred: {e}')
        return None
    
## Function to run the HTTP client   
def simple_http_client():
    ### Get the website URL
    url = get_website_url()
    ### Get the HTTP method
    method = get_http_method()
    ### Get JSON data for POST and PUT requests
    jsonData = None
    if method in [2, 3]:
        jsonData = get_json_data(1 if 'jsonplaceholder' in url else 2)
    ### Add an index for PUT and DELETE requests
    if method in [3, 4]:
        index = random.randint(1, 6)
        url += f'/{index}'
    ### Make the HTTP request
    response = make_request(url, method, jsonData)
    ### Display the response
    if response:
        print(f'Response status code: {response.status_code}')
        print('Response body:')
        try:
            print(response.json())
        except ValueError:
            print('No JSON content in response.')

## Main program
if __name__ == '__main__':
    simple_http_client()                     
                
                            
