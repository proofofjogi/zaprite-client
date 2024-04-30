
import requests


class ZapriteClient:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.headers = {
            "accept": "application/json",
            "authorization": f"Bearer {api_key}",
            "content-type": "application/json",
        }
    

    def check_currency_support(self, currency: str):
        # pulls in currency codes from api, tests currency against them
        response = requests.get('https://api.zaprite.com/openapi.json')
        data = response.json()

        # parese it ...
        # yeah ...
        # will break if they re-shuffle their api
        # better ways ????
        supported_currenies = data.get('paths').get('/v1/order').get('post').get('requestBody').get('content').get('application/json').get('schema').get('properties').get('currency').get('enum')

        # This is the list tat returns as of now: ['USD', 'BTC', 'LBTC', 'ALL', 'DZD', 'ARS', 'AMD', 'AUD', 'AZN', 'BHD', 'BDT', 'BYN', 'BMD', 'BOB', 'BAM', 'BRL', 'BGN', 'KHR', 'CAD', 'CLP', 'CNY', 'COP', 'CRC', 'HRK', 'CUP', 'CZK', 'DKK', 'DOP', 'EGP', 'EUR', 'GEL', 'GHS', 'GTQ', 'HNL', 'HKD', 'HUF', 'ISK', 'INR', 'IDR', 'IRR', 'IQD', 'ILS', 'JMD', 'JPY', 'JOD', 'KZT', 'KES', 'KWD', 'KGS', 'LBP', 'MKD', 'MYR', 'MUR', 'MXN', 'MDL', 'MNT', 'MAD', 'MMK', 'NAD', 'NPR', 'TWD', 'NZD', 'NIO', 'NGN', 'NOK', 'OMR', 'PKR', 'PAB', 'PEN', 'PHP', 'PLN', 'GBP', 'QAR', 'RON', 'RUB', 'SAR', 'RSD', 'SGD', 'ZAR', 'KRW', 'SSP', 'VES', 'LKR', 'SEK', 'CHF', 'THB', 'TTD', 'TND', 'TRY', 'UGX', 'UAH', 'AED', 'UYU', 'UZS', 'VND']
        
        if currency.upper() not in supported_currenies:
            raise Exception(f"Currency {currency} is not supported")
        else:
            # return for developer
            return True

    # create an order
    def create_order(self, amount: int, currency: str, external_uniq_id: str, redirect_url: str, label: str):

        # see if currency code is supported
        _ = self.check_currency_support(currency)
        
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

