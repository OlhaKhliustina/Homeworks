#Create a program that will ask user to search a word. 
#Search this word in Giphy (use their API). Return links to these GIFs as a result
import requests

url = 'https://api.giphy.com/v1/gifs/search'
api_key = 'guZa1VNPwZR7e9MiNLxlRZIV0Ljg5Lro'

user_gif = input('Enter what you want to search: ')
params = {
    'api_key': api_key,
    'q': user_gif,
    'limit': 5
}

response = requests.get(url, params=params)

if response.ok:
    data = response.json()['data']
    gif_urls = [gif['url'] for gif in data]
    for url in gif_urls:
        print(url)
else:
    print (f'You have {response.status_code} mistake')
