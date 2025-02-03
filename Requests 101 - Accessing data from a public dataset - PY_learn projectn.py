# Requests 101 - Accessing data from a public dataset - PY_learn projectn
## Import the HTTP liabrary
import requests

## Function to retrieve data
def fetch_users():
    ### Error Handling
    try:
        url = "https://jsonplaceholder.typicode.com/users"
        response = requests.get(url)
        response.raise_for_status()
        if response.status_code == 200:
            print('Data has been successfully retrieved :)')
        users = response.json()
        ### Display retrieved data
        for i,user in enumerate(users):
            print(f'{i + 1} Name: {user['name']} Email: {user['email']}.') 
    except requests.exceptions.RequestException as e:
        print(f'An error has occured :( {e}.')  
        
## Main function
if __name__ == '__main__':
    fetch_users()    
        
           
        
     
       