# Buycoins-SDK
Python client for Buycoins Africa's API

## Getting started
Installation via Pip:

```bash
$ pip install py-buycoins
```

# Usage
py-buycoins provides a suite of utility classes with methods that automatically generate graphql queries on behalf of the user, with specifications based off input arguments. With these classes, the generated queries can be introspected before being sent. py-buycoins also features a client class which executes the queries to the Buycoins API, over HTTP.


## Authorization
In order to use execute queries you must instantiate the client class with our access keys from the buycoins account. You'll need to provision the class with the \[PUBLIC_KEY\] and \[SECRET_KEY\] as follows:

```python
from buycoins_sdk import BuycoinsClient
import os

client = BuycoinsClient(
    public_key=os.getenv('PUB_KEY'),
    secret_key=os.getenv('SECRET_KEY')
)

```

Usually these keys are stored as environment variables, with the aid of a `.env` file, it's probably in your best interest to do so.


## Basic Usage [Buying crypto]
According the official documentation on Buycoins [here](https://developers.buycoins.africa/), in order to buy crypto we must fetch an active price ID, first using the `getPrices`. The client class also features some generic helper methods such as get_active_price_id, which can be used to fetch price IDs for the sake of orders to the API, instead of having to call the query generator classes. The query generator remains however. Once we have that ID, we can then use that to send a query via the `buy` query. We can do this using the BuyCoins class (query generator) as follows:

```python
from orders import BuyCoins

# fetches active price id for bitcoin
price_id = client.get_active_price_id(cryptocurrency='bitcoin') 

# generate query
buy = BuyCoins(
    cryptocurrency='bitcoin',
    coin_amount=0.02,
    price = price_id
).from_buycoins(response_fields=['id', 'cryptocurrency', 'status'])

# execute query
resp = client.execute(query=buy)

# OR

resp = buy.execute(client=client) # returns all response_fields from API by default
```
If you need to know what kind of fields are returned by the BuyCoins API, check the official docs [here](https://developers.buycoins.africa/).


### More Examples
```python

```

### Making Custom requests


### Note For Contributor

```requirements.txt``` is for development purposes only as regards setting up your development environment, not used in the build process of the library. Dependencies are (or will be) specified in setup.py