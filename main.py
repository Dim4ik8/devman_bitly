import requests
from urllib.parse import urlsplit
import os
from dotenv import load_dotenv


def shorten_link(url, token):
    headers = {'Authorization': f'Bearer {token}'}
    create_bitlink = 'https://api-ssl.bitly.com/v4/bitlinks'
    body = {"long_url": url}
    response = requests.post(create_bitlink, headers=headers, json=body)
    if response.ok:
        return response.json()['link']


def count_clicks(bitlink, token):
    headers = {'Authorization': token}
    parced_url = urlsplit(bitlink)
    bitlink_for_clicks = f'{parced_url.netloc}{parced_url.path}'
    url_for_clicks = f'https://api-ssl.bitly.com/v4/bitlinks/{bitlink_for_clicks}/clicks/summary'
    response = requests.get(url_for_clicks, headers=headers)
    if response.ok:
        return response.json()['total_clicks']


def is_bitlink(url, token):
    headers = {'Authorization': token}

    parced_url = urlsplit(url)
    bitlink_for_check = f'{parced_url.netloc}{parced_url.path}'

    response = requests.get(f'https://api-ssl.bitly.com/v4/bitlinks/{bitlink_for_check}', headers=headers)
    return response.ok


def main():
    load_dotenv()
    token = os.getenv('BITLY_TOKEN')

    link = input('Введите полную ссылку: ')
    bitlink = shorten_link(link, token)
    print(bitlink)

    print(is_bitlink(bitlink, token))

    clicks = count_clicks(bitlink, token)
    print(clicks)


if __name__ == '__main__':
    main()
