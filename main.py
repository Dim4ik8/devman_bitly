import requests
import json

from urllib.request import urlopen, URLError
import validators
from urllib.parse import urlsplit
import os
from dotenv import load_dotenv

load_dotenv()

token = os.getenv('TOKEN')
headers = {'Authorization': token}


def shorten_link(token, url):
    create_bitlink = 'https://api-ssl.bitly.com/v4/bitlinks'
    body = {"long_url": url}
    response = requests.post(create_bitlink, headers=headers, json=body)

    return response.json()['link']


def validate_url(url):
    if validators.url(url):
        try:
            urlopen(url)
            return True
        except URLError:
            return False
    else:
        return False


def count_clicks(bitlink):
    parced = urlsplit(bitlink)
    bitlink_for_clicks = parced[1] + parced[2]
    url_for_clicks = f'https://api-ssl.bitly.com/v4/bitlinks/{bitlink_for_clicks}/clicks/summary'
    response = requests.get(url_for_clicks, headers=headers)
    return response.json()['total_clicks']


def is_bitlink(url):
    if validate_url(url):
        parced = urlsplit(url)
        bitlink_for_check = parced[1] + parced[2]

        response = requests.get(f'https://api-ssl.bitly.com/v4/bitlinks/{bitlink_for_check}', headers=headers)
        if response.ok:
            return True
        else:
            return False
    else:
        return False


def main():
    pass


if __name__ == '__main__':
    main()
