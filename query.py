#!/usr/bin/env python3
import json
import requests
import sys
import numpy as np


def get_prices(currency, base_currency, days_ago):
    try:
        json_store = requests.get(
            f'https://api.coingecko.com/api/v3/coins/{currency}/ohlc?vs_currency={base_currency}&days={days_ago}')
        candles = json.loads(json_store.content.decode("utf-8"))
        time = np.array([item[0] for item in candles])
        openc = np.array([item[1] for item in candles])
        highc = np.array([item[2] for item in candles])
        lowc = np.array([item[3] for item in candles])
        closec = np.array([item[4] for item in candles])
        if len(time) < 1:
            print("APIs not working properly")
            exit()
    except requests.exceptions.ConnectionError:
        sys.stdout.write('Connection Error')

    return time, openc, highc, lowc, closec
