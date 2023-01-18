from urllib.parse import urljoin
import requests

API_BASE_URL = "https://api.librus.pl"
API_TOKEN = "Mjg6ODRmZGQzYTg3YjAzZDNlYTZmZmU3NzdiNThiMzMyYjE="

def base_post_rq(endpoint, body={}, access_token=None):
    if access_token is None:
        return requests.post(
            urljoin(API_BASE_URL, endpoint),
            data=body,
            headers={"Authorization": f"Basic {API_TOKEN}"},
        )
    else:
        return requests.post(
            urljoin(API_BASE_URL, endpoint),
            data=body,
            headers={"Authorization": f"Bearer {access_token}"},
        )

def base_get_rq(endpoint, access_token=None):
    if access_token is None:
        return requests.get(
            urljoin(API_BASE_URL, endpoint),
            headers={"Authorization": f"Basic {API_TOKEN}"},
        )
    else:
        return requests.get(
            urljoin(API_BASE_URL, endpoint),
            headers={"Authorization": f"Bearer {access_token}"},
        )
