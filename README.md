# PyLibrus

[![Stand With Ukraine](https://raw.githubusercontent.com/vshymanskyy/StandWithUkraine/main/badges/StandWithUkraine.svg)](https://stand-with-ukraine.pp.ua)
![License MIT](https://img.shields.io/github/license/ChimekKoo/pylibrus)

Librus (polish school e-register) unofficial API client written in Python.

# Installation
Clone the repo and use `pylibrus` folder as the module.
PIP package is not available yet.

# Usage
(Replace every field containing 'your' with your data)
## Authorization
- Authorize using existing token (load existing tokens pair)  
or
- Generate new OAuth token  
    - using user credentials:
        ```python
        import pylibrus
        access_token, refresh_token = pylibrus.auth.user_credentials(
            username="yourusername",
            password="yourpassword",
            long_lived=True # optional, if set to True (default) token will be valid for 24h, if set to False token will be valid for 3h
        )
        print(
            access_token, # used to access resources
            refresh_token # used to regenerate access token without user credentials
        )
        ```
    - using previousely generated refresh token:
        ```python
        import pylibrus
        access_token, refresh_token = pylibrus.auth.refresh_token(
            refresh_token="yourrefreshtoken",
            long_lived=True # default True (if not specified)
        )
        print(access_token, refresh_token)
        ```
## Accessing resources
Access resources using previousely generated access token (see [Authorization](#authorization)):
```python
import pylibrus
lib = pylibrus.Librus("youraccesstoken") # previousely generated/cached access token
json_res = lib.getResource("YourResourceName")
print(json_res) # Raw API response (decoded JSON as dict)
```
List of available resources [here](resources.txt).
## Examples
Get user name using login/password authorization:
```python
import pylibrus
lib = pylibrus.Librus(pylibrus.auth.user_credentials(
    username="yourusername",
    password="yourpassword",
)[0])
names = lib.getResource("Me")["Me"]["User"]
print(f"Hello {names['FirstName']} {names['LastName']}")
```
Get number of user's grades using new access token generated using previousely cached refresh token:
```python
import pylibrus
lib = pylibrus.Librus(pylibrus.auth.refresh_token(
    refresh_token="yourrefreshtoken"
)[0])
grades = lib.getResource("Grades")["Grades"]
print(len(grades))
```
# Contribute
Any pull requests are welcome.
