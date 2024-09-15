# Георгий Дубров, 21-я когорта — Финальный проект. Инженер по тестированию плюс
import configuration
import requests
import data
import new_order

# Создание заказа
def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                         json=body)
response = post_new_order(data.order_body)

# Сохранить номер трека заказа.
def get_track(track):
    return requests.get(configuration.URL_SERVICE + configuration.FIND_ORDER_FROM_TRACK_PATH + str(track))

# Выполнить запрос на получения заказа по треку заказа.
def checking_code():
    response = new_order.post_new_order(data.order_body)
    track = response.json()["track"]
    return get_track(track).status_code

# Проверить, что код ответа равен 200.
def test_asserting_200():
    assert checking_code() == 200