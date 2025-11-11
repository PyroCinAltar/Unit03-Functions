# Q1
'''
4
7000
'''

# Q2
'''
0x9F1aB3c...
'''

# Q3

def portfilio_value(holdings, prices):
    total = 0.00
    for coin_type, asset_amount in holdings.items():
        total += asset_amount * prices[coin_type]
    return round(total, 2)

holdings_dict = {'BTC': 0.5, "ETH": 8.2, "SOL": 50}
prices_dict = {'BTC': 62400, "ETH": 2480, "SOL": 142}

print(portfilio_value(holdings_dict, prices_dict))