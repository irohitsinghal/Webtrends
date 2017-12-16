from coinbase.wallet.client import Client

api_key = 'PM2DQtwbsXLez92A'
api_secret = 'cdkT3HNPKIqMPGPn38cQ0ecHfoAf997J'
client = Client(api_key, api_secret, api_version='YYYY-MM-DD')

currency_code = 'INR'  # can also use EUR, CAD, etc.

# Make the request online
price = client.get_spot_price(currency=currency_code)

print('Current bitcoin price in %s: %s' % (currency_code, price.amount))
