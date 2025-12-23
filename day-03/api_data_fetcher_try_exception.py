import requests
import json

Apikey = "W5080QXBNUJ6HVTC"
symbol = "IBM"
stock_api = "https://www.alphavantage.co/query"
querry = f"{stock_api}?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={Apikey}"

try:
    response = requests.get(url=stock_api+querry, timeout=10)
    response.raise_for_status()
    
    data = response.json()
    print(json.dumps(data, indent=4))
    
    filename = f"{symbol}_stock_data.json"
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)
    
    print(f"\n✓ Data saved to {filename}")
    
    
    # UNCOMMENT BELOW CODE FOR STOCK ANALYSIS WITH IF-ELIF-ELSE
    
    print("\n" + "=" * 50)
    print("METADATA")
    print("=" * 50)
    metadata = data["Meta Data"]
    print(f"Information: {metadata['1. Information']}")
    print(f"Symbol: {metadata['2. Symbol']}")
    print(f"Last Refreshed: {metadata['3. Last Refreshed']}")
    print(f"Output Size: {metadata['4. Output Size']}")
    print(f"Time Zone: {metadata['5. Time Zone']}")
    
    time_series = data["Time Series (Daily)"]
    latest_date = list(time_series.keys())[0]
    
    print("\n" + "=" * 50)
    print(f"LATEST STOCK DATA ({latest_date})")
    print("=" * 50)
    date_data = time_series[latest_date]
    open_price = float(date_data['1. open'])
    high_price = float(date_data['2. high'])
    low_price = float(date_data['3. low'])
    close_price = float(date_data['4. close'])
    volume = int(date_data['5. volume'])
    
    print(f"Open: ${open_price}")
    print(f"High: ${high_price}")
    print(f"Low: ${low_price}")
    print(f"Close: ${close_price}")
    print(f"Volume: {volume:,}")
    
    print("\n" + "=" * 50)
    print("STOCK ANALYSIS")
    print("=" * 50)
    
    price_change = close_price - open_price
    if price_change > 0:
        print(f"✓ Stock GAINED ${price_change:.2f} ({(price_change/open_price)*100:.2f}%)")
    elif price_change < 0:
        print(f"✗ Stock LOST ${abs(price_change):.2f} ({(price_change/open_price)*100:.2f}%)")
    else:
        print("→ Stock remained UNCHANGED")
    
    if volume > 5000000:
        print(f"📊 HIGH trading volume: {volume:,} shares")
    elif volume > 3000000:
        print(f"📊 MODERATE trading volume: {volume:,} shares")
    else:
        print(f"📊 LOW trading volume: {volume:,} shares")
    
    volatility = high_price - low_price
    if volatility > 5:
        print(f"⚠️  HIGH volatility: ${volatility:.2f} price range")
    elif volatility > 2:
        print(f"⚡ MODERATE volatility: ${volatility:.2f} price range")
    else:
        print(f"✓ LOW volatility: ${volatility:.2f} price range")
    
    print("=" * 50)
    
except requests.exceptions.Timeout:
    print("Error: Request timed out. Please try again.")
except requests.exceptions.ConnectionError:
    print("Error: Network connection failed. Check your internet.")
except requests.exceptions.HTTPError as e:
    print(f"Error: HTTP error occurred: {e}")
except json.JSONDecodeError:
    print("Error: Failed to parse JSON response.")
except FileNotFoundError:
    print("Error: File path not found.")
except PermissionError:
    print("Error: Permission denied to write file.")
except Exception as e:
    print(f"Error: An unexpected error occurred: {e}")
