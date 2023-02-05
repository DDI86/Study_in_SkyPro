import random
import requests


def load_random_word():
    """Получение данных со стороннего ресурса в фрмате JSON"""
    response = requests.get('https://jsonkeeper.com/b/K9GD')
    return random.choice(response.json())
