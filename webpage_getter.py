import bs4
import requests


def get_response(url_to_get: str) -> requests.Response:
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/74.0.3729.169 Safari/537.36",
        'referer': 'https://www.google.com/'
    }

    return requests.get(url_to_get, headers=headers)


def get_soup(response_to_parse: requests.Response) -> bs4.BeautifulSoup:
    return bs4.BeautifulSoup(response_to_parse.text, features="html.parser")
