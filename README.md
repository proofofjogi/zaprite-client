# Zaprite python client

This python client is intended to interface with the <a href="https://api.zaprite.com/#overview">zaprite api</a>

## Usage:

No pip package available yet, make a sub-folder `zaprite` and put the init file there: `zaprite/__init__.py`.
Then you can import it:
```
from zaprite import ZapriteClient
```
To instantiate the client, pass your api key to it:

```
api_key = "YOUR_API_KEY_HERE"
zaprite = ZapriteClient(api_key)
```

Then you can create an order

```
amount = 1000
currency = "USD"
external_uniq_id = "order123"
redirect_url = "https://example.com/callback"
label = "Test Order"
order_response = zaprite.create_order(amount, currency, external_uniq_id, redirect_url, label)
```


