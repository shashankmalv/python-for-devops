import requests
import json

Apikey = "W5080QXBNUJ6HVTC"
symbol = "IBM"
stock_api = "https://www.alphavantage.co/query"
querry = f"{stock_api}?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={Apikey}"

response = requests.get(url=stock_api+querry)

if response.status_code == 200:
    data = response.json()
    print(json.dumps(data, indent=4))
    
    filename = f"{symbol}_stock_data.json"
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)
    
    print(f"\n✓ Data saved to {filename}")
else:
    print(f"Error: Failed to fetch data. Status code: {response.status_code}")
