'''
- Вивезти з API(я взяла НБУ) курс валют для:
USA
EURO
GBR
PLN
Свою валюту
- Написати Test
- Вивезти курс валюти від користувача
- Робити перевірки на status code
- Написати це функцію
- Залити на git(flake8 use, requirments, )

'''

import requests

exch_nbu = requests.get('https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json')
assert exch_nbu.status_code == 200


def exchange():
    my_currencies = {
        840: 'Американський долар', 
        978: 'Євро', 
        826: 'Британський фунт', 
        985: 'Польський злотий', 
        348: 'Угорський форинт'}
    my_rates = []
    for obj in exch_nbu.json():
        if obj['r030'] in my_currencies and obj not in my_rates:
            my_rates.append(obj)
            print(f"Валюта: {my_currencies[obj['r030']]} | Купівля {obj['rate']}")


def user_exchange(user_currency):
    kurs = user_currency.upper()
    for obj in exch_nbu.json():
        if obj['cc'] == kurs:
            print(f"Валюта: {obj['cc']} | Купівля {obj['rate']}")
        else:
            pass
