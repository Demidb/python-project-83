from urllib.parse import urlparse

from validator_collection import validators

MAX_URL_LEN = 255


def normalize_url(url: str) -> str:
    parsed_url = urlparse(url)
    return f'{parsed_url.scheme}://{parsed_url.netloc}'


def validate_url(url: str) -> list[str]:
    errors = []
    if url == '':
        errors.append('No url')

    if errors or not validators.url(url) or len(url) > MAX_URL_LEN:
        errors.append('Not valid url')

    return errors