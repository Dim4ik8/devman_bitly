import requests
from pprint import pprint
from urllib.request import urlopen, URLError
from urllib.parse import urlsplit
import os
from dotenv import load_dotenv


def shorten_link(url, token):
    headers = {'Authorization': token}
    create_bitlink = 'https://api-ssl.bitly.com/v4/bitlinks'
    body = {"long_url": url}
    response = requests.post(create_bitlink, headers=headers, json=body)
    response.raise_for_status()
    return response.json()['link']


def count_clicks(bitlink, token):
    headers = {'Authorization': token}
    parced_url = urlsplit(bitlink)
    bitlink_for_clicks = f'{parced_url[1]}{parced_url[2]}'
    url_for_clicks = f'https://api-ssl.bitly.com/v4/bitlinks/{bitlink_for_clicks}/clicks/summary'
    response = requests.get(url_for_clicks, headers=headers)

    return response.json()['total_clicks']


def is_bitlink(url, token):
    headers = {'Authorization': token}

    parced_url = urlsplit(url)
    bitlink_for_check = f'{parced_url.netloc}{parced_url.path}'

    response = requests.get(f'https://api-ssl.bitly.com/v4/bitlinks/{bitlink_for_check}', headers=headers)
    if response.ok:
        return response.json()


def main():
    load_dotenv()
    TOKEN = os.getenv('BITLY_TOKEN')


if __name__ == '__main__':
    main()
