import configuration
import data
import requests

def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                         json=body)
response = post_new_order(data.order_body)
print(response.status_code)
print(response.json())