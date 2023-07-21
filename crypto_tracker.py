import requests
import time

def get_cryptocurrency_price(crypto_symbol):
    url = f'https://api.coingecko.com/api/v3/simple/price?ids={crypto_symbol}&vs_currencies=usd'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data.get(crypto_symbol.lower(), {}).get('usd')
    else:
        return None

if __name__ == "__main__":
    cryptocurrencies = ['bitcoin', 'ethereum', 'litecoin']  # Add more cryptocurrencies as needed

    while True:
        print("\nCurrent Prices:")
        for crypto in cryptocurrencies:
            price = get_cryptocurrency_price(crypto)
            if price:
                print(f"{crypto.capitalize()}: ${price}")
            else:
                print(f"Error fetching {crypto} price.")

        # Refresh every 10 seconds
        time.sleep(10)
