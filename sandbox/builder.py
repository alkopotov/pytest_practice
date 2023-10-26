from settings import base_settings
from client import HTTPClient


def get_http_client(base_url: str = base_settings.api_url) -> HTTPClient:
    return HTTPClient(base_url=base_url, trust_env=True)
