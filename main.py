import os
from urllib import parse

import requests
from dotenv import load_dotenv

API_URL = "https://api-ssl.bitly.com/v4/bitlinks/"


def shorten_link(token, url) -> str:
    """Func returns bitlink for URL"""
    payload = {"long_url": url, "group_guid": "Bm8niFbY79l", "domain": "bit.ly"}
    headers = {"Authorization": token}
    response = requests.post(API_URL, headers=headers, json=payload)
    response.raise_for_status()
    bitlink = response.json()["id"]
    return f"Your bitlink: {bitlink}"


def count_links(token, url) -> str:
    """Func returns quantity of bitlink cliks"""
    endpoint = "{}/clicks/summary".format(url)
    api_url_clicks = parse.urljoin(API_URL, endpoint)
    headers = {"Authorization": token}
    response = requests.get(api_url_clicks, headers=headers)
    response.raise_for_status()
    clicks_count = response.json()["total_clicks"]
    return f"Bitlink clicks: {clicks_count}"


def is_bitlink(url, token):
    """Check url, is bitlink or not"""
    parsed_url = parse.urlparse(url)
    url_without_scheme = parsed_url.netloc + parsed_url.path
    api_url_check = parse.urljoin(API_URL, url_without_scheme)
    headers = {"Authorization": token}
    response = requests.get(api_url_check, headers=headers)
    return response.ok


# def check_link(url):
#     """check response status, if it is not Ok, raise exception"""
#     response = requests.get(url)
#     response.raise_for_status()


def main():
    if is_bitlink(url, token):
        try:
            clicks_count = count_links(token, url)
        except requests.exceptions.HTTPError:
            print("The link is wrong, please check it")
        else:
            print(clicks_count)
    else:
        try:
            bitlink = shorten_link(token, url)
        except requests.exceptions.HTTPError:
            print("The link is wrong, please check it")
        else:
            print(bitlink)


if __name__ == "__main__":
    load_dotenv()
    token = os.environ["API_BITLY_TOKEN"]
    url = input("Enter url:")
    main()
