import requests
from dotenv import load_dotenv
import os


def shorten_link(token, url) -> str:
    """Func returns bitlink for URL"""
    api_url = "https://api-ssl.bitly.com/v4/bitlinks"
    payload = {"long_url": url, "group_guid": "Bm8niFbY79l", "domain": "bit.ly"}
    headers = {"Authorization": token}
    response = requests.post(api_url, headers=headers, json=payload)
    response.raise_for_status()
    bitlink = response.json()['id']
    return f"Your bitlink: {bitlink}"


def count_links(token, url) -> str:
    """Func returns quantity of bitlink cliks"""
    url = "https://api-ssl.bitly.com/v4/bitlinks/{}/clicks/summary".format(url)
    headers = {"Authorization": token}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    clicks_count = response.json()['total_clicks']
    return f"Bitlink clicks: {clicks_count}"


def is_bitlink(url, token):
    """Check url, bitlink for errors"""
    api_url = "https://api-ssl.bitly.com/v4/bitlinks/{}".format(url)
    headers = {"Authorization": token}
    response = requests.get(api_url, headers=headers)
    if response.ok:
        try:
            clicks_count = count_links(token, url)
        except requests.exceptions.HTTPError as error:
            status_code_error = error.response.status_code
            text_error = error.response.text
            return status_code_error, text_error
        else:
            return clicks_count
    else:
        try:
            bitlink = shorten_link(token, url)
        except requests.exceptions.HTTPError as error:
            status_code_error = error.response.status_code
            text_error = error.response.text
            return status_code_error, text_error
        else:
            return bitlink


if __name__ == "__main__":
    load_dotenv()
    token = os.environ['API_BITLY_TOKEN']
    url = input("Enter url:")
    print(is_bitlink(url, token))

