
import requests


def test_currency_support(currency):
    # not ideal like this
    # TODO pull in from api endpoint at https://api.zaprite.com/openapi.json
    supported_currenies = ["USD","BTC","LBTC","ALL","DZD","ARS","AMD","AUD","AZN","BHD","BDT","BYN","BMD","BOB","BAM","BRL","BGN","KHR","CAD","CLP","CNY","COP","CRC","HRK","CUP","CZK","DKK","DOP","EGP","EUR","GEL","GHS","GTQ","HNL","HKD","HUF","ISK","INR","IDR","IRR","IQD","ILS","JMD","JPY","JOD","KZT","KES","KWD","KGS","LBP","MKD","MYR","MUR","MXN","MDL","MNT","MAD","MMK","NAD","NPR","TWD","NZD","NIO","NGN","NOK","OMR","PKR","PAB","PEN","PHP","PLN","GBP","QAR","RON","RUB","SAR","RSD","SGD","ZAR","KRW","SSP","VES","LKR","SEK","CHF","THB","TTD","TND","TRY","UGX","UAH","AED","UYU","UZS","VND"]
    if currency in supported_currenies:
        return True
    else:
        return False
    


class ZapriteClient:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.headers = {
            "accept": "application/json",
            "authorization": f"Bearer {api_key}",
            "content-type": "application/json",
        }

    # create an order
    def create_order(self, amount: int, currency: str, external_uniq_id: str, redirect_url: str, label: str):

        # see if currency code is supported
        # raise exception if not
        is_supported = test_currency_support(currency)
        if not is_supported:
            raise Exception(f"Currency {currency} is not supported")
        
        url = "https://api.zaprite.com/v1/order"
        data = {
            "amount": amount,
            "currency": currency,
            "externalUniqId": external_uniq_id,
            "redirectUrl": redirect_url,
            "label": label,
        }

        response = requests.post(url, headers=self.headers, json=data)

        if response.ok:
            return response.json()
        else:
            raise Exception(f"API request failed with status {response.status_code}")


    # Get an order by ID (Zaprite ID or externalUniqId)
    def get_order_by_id(self, order_id: str):
        url = f"https://api.zaprite.com/v1/order/{order_id}"
        
        response = requests.get(url, headers=self.headers)

        if response.ok:
            return response.json()
        else:
            raise Exception(f"API request failed with status {response.status_code}")

