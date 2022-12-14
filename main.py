import requests
from urllib.parse import urlsplit
import os
from dotenv import load_dotenv
import argparse


def shorten_link(url, token):
    headers = {'Authorization': f'Bearer {token}'}
    link = 'https://api-ssl.bitly.com/v4/bitlinks'
    body = {"long_url": url}
    response = requests.post(link, headers=headers, json=body)
    response.raise_for_status()
    return response.json()['link']


def count_clicks(link, token):
    headers = {'Authorization': token}
    parced_url = urlsplit(link)
    bitlink = f'{parced_url.netloc}{parced_url.path}'
    url = f'https://api-ssl.bitly.com/v4/bitlinks/{bitlink}/clicks/summary'
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    quantity = response.json()['total_clicks']
    return f'Количество переходов по ссылке Битли: {quantity}'


def is_bitlink(url, token):
    headers = {'Authorization': token}

    parced_url = urlsplit(url)
    bitlink = f'{parced_url.netloc}{parced_url.path}'

    response = requests.get(f'https://api-ssl.bitly.com/v4/bitlinks/{bitlink}', headers=headers)
    return response.ok


def main():
    load_dotenv()
    token = os.getenv('BITLY_TOKEN')

    parser = argparse.ArgumentParser(
        description='Скрипт для сокращения ссылок'
    )
    parser.add_argument('link', help='Введите любую ссылку в формате http://yandex.ru')

    args = parser.parse_args()
    link = args.link

    if is_bitlink(link, token):
        clicks = count_clicks(link, token)
        print(clicks)
    else:
        bitlink = shorten_link(link, token)
        print(bitlink)


if __name__ == '__main__':
    main()
