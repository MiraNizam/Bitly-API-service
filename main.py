import os
from urllib import parse

import requests
from dotenv import load_dotenv
import argparse


API_URL = "https://api-ssl.bitly.com/v4/bitlinks/"


def add_argument():
    """create parser to add the links"""
    parser = argparse.ArgumentParser()
    parser.add_argument('url', help="add an url to start using API-service")
    return parser.parse_args()


def shorten_link(token, url) -> str:
    """Func returns bitlink for URL"""
    payload = {"long_url": url}
    headers = {"Authorization": token}
    response = requests.post(API_URL, headers=headers, json=payload)
    response.raise_for_status()
    bitlink = response.json()["id"]
    return bitlink


def count_links(token, url) -> str:
    """Func returns quantity of bitlink cliks"""
    endpoint = "{}/clicks/summary".format(url)
    api_url = parse.urljoin(API_URL, endpoint)
    headers = {"Authorization": token}
    response = requests.get(api_url, headers=headers)
    response.raise_for_status()
    total_clicks = response.json()["total_clicks"]
    return total_clicks


def is_bitlink(url: str, token: str) -> bool:
    """Check url and return True if itis a bitlink"""
    parsed_url = parse.urlparse(url)
    url_without_scheme = "{}{}".format(parsed_url.netloc, parsed_url.path)
    api_url = parse.urljoin(API_URL, url_without_scheme)
    headers = {"Authorization": token}
    response = requests.get(api_url, headers=headers)
    return response.ok


def main():
    load_dotenv()
    token = os.environ["API_TOKEN"]
    args = add_argument()
    url = args.url

    if is_bitlink(url, token):
        try:
            total_clicks = count_links(token, url)
        except requests.exceptions.HTTPError:
            print("The link is wrong, please check")
        else:
            print(f"Bitlink clicks: {total_clicks}")
    else:
        try:
            bitlink = shorten_link(token, url)
        except requests.exceptions.HTTPError:
            print("The bitlink is invalid or access denied, please check")
        else:
            print(f"Your bitlink: {bitlink}")


if __name__ == "__main__":
    main()
