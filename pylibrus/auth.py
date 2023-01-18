from pylibrus.api import base_get_rq, base_post_rq

class Token:
    def __init__(self, access_token, refresh_token, verify=True):
        if verify:
            res = base_get_rq("/2.0/Me", access_token=access_token)
            if res.status_code != 200:
                raise pylibrus.exceptions.InvalidCredentials("Invalid access token.")
                return
        self.access_token = access_token
        self.refresh_token = refresh_token
    def __str__(self):
        return str({"access_token": self.access_token, "refresh_token": self.refresh_token})
    def __getitem__(self, key):
        if key == "access_token":
            return self.access_token
        elif key == "refresh_token":
            return self.refresh_token
        else:
            raise KeyError("Invalid key. The only available are 'access_token' and 'refresh_token'.")
            return

def user_credentials(username, password, long_lived=True):
    res = base_post_rq("/OAuth/Token", body={
        "username": username,
        "password": password,
        "grant_type": "password",
        "librus_long_term_token": int(long_lived),
    })
    if res.status_code != 200:
        raise pylibrus.exceptions.InvalidCredentials("Invalid credentials.")
        return
    access_token, refresh_token = res.json()["access_token"], res.json()["refresh_token"]
    return Token(access_token, refresh_token, verify=False)

def refresh_token(refresh_token, long_lived=True):
    res = base_post_rq("/OAuth/Token", body={
        "refresh_token": refresh_token,
        "grant_type": "refresh_token",
        "librus_long_term_token": int(long_lived),
    })
    if res.status_code != 200:
        raise pylibrus.exceptions.InvalidCredentials("Invalid refresh token.")
        return
    access_token, refresh_token = res.json()["access_token"], res.json()["refresh_token"]
    return Token(access_token, refresh_token, verify=False)
