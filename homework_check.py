# import logging
import os
import time

import requests
from dotenv import load_dotenv
from pprint import pprint
from math import ceil

load_dotenv()
secret_token = os.getenv('TOKEN')
current_time = time.time()

url = 'https://practicum.yandex.ru/api/user_api/homework_statuses/'
headers = {'Authorization': f'OAuth {secret_token}'}
payload = {'from_date': ceil(current_time)}

homework_statuses = requests.get(url, headers=headers, params=payload)

pprint(homework_statuses.json())
