# Buycoins-SDK
Python client for Buycoins Africa's API

## Getting started
Installation via Pip:

```bash
$ pip install buycoins-sdk
```

# Usage
buycoins-sdk has a client class (BuycoinsClient) that handles all forms of requests via certain available methods. Consider this methods, to be already made queries on your behalf to the buycoins API. You can look at the official BuyCoins API docs [here](https://developers.buycoins.africa/)

### Available Handler Methods in client Class
* get_sale_price()
* create_address()
* get_dynamic_price()
* get_orders()
* get_market_book()
* create_deposit_account()
* get_network_fee()
* get_balance()
* buy()
* post_limit_order()
* post_market_order()
* sell()
* send()
* receive()

## Authorization
In order to use any of the methods and safely send requests to Buycoins you must instantiate the client class, with your generated keys \[PUBLIC_KEY\] and \[SECRET_KEY\] as follows:

```python
from buycoins_sdk import BuycoinsClient
import os

client = BuycoinsClient(
    public_key=os.getenv('PUB_KEY'),
    secret_key=os.getenv('SECRET_KEY')
)

```

Usually these keys are stored as environment variables, with the aid of a `.env` file, it's probably in your best interest to do so.


## Basic Usage
With the new client instance we've created we now have access to all handler methods, lets see how to buy crypto from buycoins. To buy we invoke the buy() method of the client class, as follows:

```python
# fetch current price of bitcoin
price = client.buy(
    coin_amount=0.002,
    cryptocurrency="bitcoin"
)
```
This request would return a number of subfields from the graphql response, by default, however you may not want all of the fields, as such you are at liberty to provision a "subfields" arguments, which is an array of strings, corresponding to the names of fields you want in the response body. For example:

```python
# fetch current price of bitcoin
price = client.buy(
    coin_amount=0.002,
    cryptocurrency="bitcoin",
    subfields=[
        "id",
        "cryptocurrency",
        "status",
        "totalCoinAmount"
    ]
)
```
If you need to know what kind of fields are returned by the BuyCoins API, check the official docs [here](https://developers.buycoins.africa/).

### Making Custom requests


### Note For Contributor

```requirements.txt``` is for development purposes only as regards setting up your development environment, not used in the build process of the library. Dependencies are (or will be) specified in setup.py