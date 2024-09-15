import configuration
import data
import requests


def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_COURIER,
                         json=body)
response = post_new_user(data.user_body)
print(response.status_code)
print(response.json())