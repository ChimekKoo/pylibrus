from pylibrus.api import base_get_rq, base_post_rq
from pylibrus.exceptions import *
from urllib.parse import quote as urlencode

class Librus:
    def __init__(self, token):
        self.token = token
    def getResource(self, name):
        res = base_get_rq("/2.0/{}".format(urlencode(name, safe="/?&")), access_token=self.token.access_token)
        if res.status_code != 200:
            raise APIError(f"Status code: {res.status_code}, Response: {res.json()}")
            return
        return res.json()
