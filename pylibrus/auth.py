from pylibrus.api import base_get_rq, base_post_rq

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
    return access_token, refresh_token

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
    return access_token, refresh_token
