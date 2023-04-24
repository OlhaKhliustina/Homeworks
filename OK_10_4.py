# 3. Вивеcти всіх космонавтів(кількість і імена) http://api.open-notify.org/astros.json
import requests

astronauts = requests.get('http://api.open-notify.org/astros.json')
assert astronauts.status_code == 200
data = astronauts.json()
print(f'Кількість космонавтів на орбіті: {data["number"]}')
for person in data['people']:
    print(person['name'])
