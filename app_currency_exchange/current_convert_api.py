from unittest import result
from django.shortcuts import redirect
import requests

from currency_exchange_rate.settings import CURRENCY_API

def get_currency_json():
    r = requests.get(f'https://api.fastforex.io/fetch-all?api_key={CURRENCY_API}')
    if r.status_code == 200:
        currency_dict = r.json()
        currency_list = tuple(zip(currency_dict['results'].values(), currency_dict['results']))
        return currency_list
    result = ((1, 'Connection error, try latter'), (1, 'Connection error, try latter'))
    return result