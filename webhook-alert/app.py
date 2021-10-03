import requests, json
from chalice import Chalice

app = Chalice(app_name='webhook-alert')     # Creates Chalice instance (AWS Lambda)

API_KEY = 'YOUR API KEY'
SECRET_KEY = 'YOUR API KEY'
BASE_URL = "https://paper-api.alpaca.markets"   # Alpaca URL   
ORDERS_URL = "{}/v2/orders".format(BASE_URL)    # Routes to Alpaca order URL
HEADERS = {'APCA-API-KEY-ID': API_KEY, 'APCA-API-SECRET-KEY': SECRET_KEY}   # Header parameters

@app.route('/buy_stock', methods=['POST'])      # Buy stock route that sends and recieves data
def buy_stock():                                
    webhook_request = app.current_request       # Gets webhook alert as JSON message
    webhook_alert = webhook_request.json_body   # Translates request to parsable JSON 

    data = {                                # Initializes JSON message to send to Alpaca API
        "symbol": webhook_alert['ticker'],  # Gets symbol from webhook alert
        "qty": 1,                           # Sets quantity to 1 stock (can also be configured from webhook alert)
        "side": "buy",                      
        "type": "limit",
        "limit_price": webhook_alert['close'],
        "time_in_force": "gtc",
        "order_class": "bracket",
        "take_profit": {
            "limit_price": webhook_alert['close'] * 1.05    # Sell for profit when profit is over 5%
        },
        "stop_loss": {
            "stop_price": webhook_alert['close'] * 0.98,    # Cut loses if 2% is lost
        }
    }

    send_data = requests.post(ORDERS_URL, json=data, headers=HEADERS)   # Sends data to Alpaca API to order stock

    alpaca_response = json.loads(send_data.content)    # Returns Alpaca's response

    # Returns confirmation info 
    return {     
        'webhook_alert': webhook_alert,
        'id': alpaca_response['id'],
        'client_order_id': alpaca_response['client_order_id']
    }
