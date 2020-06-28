import requests, json
from chalice import Chalice

app = Chalice(app_name='webhook-alert')     # Creates Chalice instance

API_KEY = 'YOUR-API-KEY'                        # Alpaca account API key
SECRET_KEY = 'YOUR-SECRET-API-KEY'              # Alpaca account secret key
BASE_URL = "https://paper-api.alpaca.markets"   # Alpaca URL   
ORDERS_URL = "{}/v2/orders".format(BASE_URL)    # Routes to Alpaca order URL
HEADERS = {'APCA-API-KEY-ID': API_KEY, 'APCA-API-SECRET-KEY': SECRET_KEY}   # Header parameters

@app.route('/buy_stock', methods=['POST'])  # Buy stock route that sends and recieves data
def buy_stock():                            # Defines buy stock page
    webhook-request = app.current_request   # Gets webhook alert as JSON message
    webhook-alert = request.json_body       # Translates webhook alert to dictionary

    data = {                                # Initializes data dictionary
        "symbol": webhook-alert['ticker'],  # Gets symbol of webhook alert
        "qty": 1,                           # Sets quantity to 1 stock
        "side": "buy",                      # Buy parameter
        "type": "limit",
        "limit_price": webhook-alert['close'],
        "time_in_force": "gtc",
        "order_class": "bracket",
        "take_profit": {
            "limit_price": webhook-alert['close'] * 1.05    # Sell for profit when profit is over 5%
        },
        "stop_loss": {
            "stop_price": webhook-alert['close'] * 0.98,    # Cut loses if 2% is lost
        }
    }

    send_data = requests.post(ORDERS_URL, json=data, headers=HEADERS)   # Sends data to Alpaca API to order stock

    alpaca_response = json.loads(send_data.content)    # Returns Alpaca's response

    # Returns confirmation info 
    return {     
        'webhook-alert': webhook-alert,
        'id': response['id'],
        'client_order_id': response['client_order_id']
    }
