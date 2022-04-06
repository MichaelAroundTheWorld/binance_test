from binance.client import Client

api_key = 'None'
api_secret = 'None'

def get_api_key():
    value = input('Write your API_KEY')
    value = api_key
    print('{type(value)}')
    return api_key
client = Client(api_key, api_secret)

