"""
1.	В python-е при помощи модулей requests, json и sys выполнить последовательность запросов (авторизация, получение списка товаров, покупка).
2.	На вход подаем номер товара и его количество
3.	Проверить, что сумма рассчитана верно и вернуть Ок, если все верно и Ошибку, если сумма не совпадает с ожидаемой

Имеются данные для логина:
email: aaa@ya.ru
password: 111

В ассортименте четыре вида товаров, при покуке от 3 штук - скидка 10%, при покупке 100 штук и более - скидка не работает
"""


import requests
import json
import sys

url = "https://webqa.mercdev.com/"
url_login = url + "login"
url_api_login = url + "api/v1/user/login"
url_api_product = url + "api/v1/product/"
# url_api_buy = url + "api/v1/order/createAndPay"
url_api_buy = "https://webqa.mercdev.com/api/v1/order/createAndPay"


email = "aaa@ya.ru"
password = "111"

card = {
    "number": "4211253802181969",
    "name": "YURII MARKIN",
    "date": "11:25",
    "cvv": "111"
}

def main():
    ids = []
    quantities = []
    products =[]

    for id in sys.argv[1::2]:
        ids.append(str(id))
    for quantity in sys.argv[2::2]:
        quantities.append(int(quantity))
    for id, quantity in zip(ids, quantities):
        products.append({"id": id, "quantity": quantity})

    json_args = json.dumps({"card" : card, "products" : products})
    # Запрос токена (логин)
    login_api_request = requests.post(url=url_api_login, data = {"email": email, "password": password})
    
    token = ((login_api_request.text)).split(sep=':' )[1].split('}')[0].strip('"')
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization" : token
    }
    # Запрос списка товаров
    product_api_request = requests.get(url=url_api_product, headers=headers, data={})
    if product_api_request.status_code != 200:
        print("Не получен список товаров")
    # Покупка товаров
    buy_api_request = requests.post(url=url_api_buy, headers=headers, data=json_args)

    #Небольшое упрощение для более коротких обращений
    d = json.loads(buy_api_request.text)
    pr = json.loads(buy_api_request.text)['transaction']['order']['products']
    
    espected_sum = 0
    qua = 0
    for p in pr:
        qua +=  p['quantity'] 
        espected_sum += p['product']['price'] * p['quantity']
    if qua > 2:
        espected_sum -= espected_sum * 0.1
    fact_sum = str(int(espected_sum))

    if fact_sum in d['message']:
        print("OK")
    else:
        print("Error")  


if __name__ == "__main__":
    main()

