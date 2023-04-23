#!/usr/bin/env python3
import json
import requests
import sys
import numpy as np
import time as time_


def getPricesCG(currency, base_currency, days_ago):
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
            print("CoinGecko APIs not working properly:")
            print(json_store)
            exit()
    except requests.exceptions.ConnectionError:
        sys.stdout.write('Connection Error')

    return time, openc, highc, lowc, closec


def getPricesPolygon(stock, base_currency, days_ago, APIKEY):
    if len(APIKEY) < 1:
        print("Plese create a APIKEY token at https://polygon.io/stocks")
        print("Insert in CliChart script at line 6")
        print("if you are trying to display cryptocurrency doublecheck the id")
        exit()
    stock = stock.upper()
    start = round(time_.time())*1000 - 24*60*60*1000
    end = start - int(days_ago)*24*60*60*1000

    if int(days_ago) <= 7:
        range = "minute"
    elif int(days_ago) <= 14 and int(days_ago) > 7:
        range = "hour"
    elif int(days_ago) >= 14:
        range = "day"
    if base_currency != 'usd':
        print("Only usd supported for stocks")
        print("Please use: <-b usd> if you are looking for stock")
        print("or doublecheck the cryptocurrency id")
        exit()
    try:
        json_store = requests.get(
            f'https://api.polygon.io/v2/aggs/ticker/{stock}/range/1/{range}/{end}/{start}?adjusted=false&sort=asc&limit=400&apiKey={APIKEY}')
        wholeResponse = json.loads(json_store.content.decode("utf-8"))
        if 'results' in wholeResponse:
            candles = wholeResponse["results"]
        else:
            print("Polygon.io APIs not working properly")
            print("Check if stock ticker is spelled properly")
            exit()

        time = np.array([item["t"] for item in candles])
        openc = np.array([item["o"] for item in candles])
        highc = np.array([item["h"] for item in candles])
        lowc = np.array([item["l"] for item in candles])
        closec = np.array([item["c"] for item in candles])
        if int(wholeResponse['queryCount']) < 1:
            print("Polygon.io APIs not working properly")
            print("Check if stock ticker is spelled properly")
            exit()
    except requests.exceptions.ConnectionError:
        sys.stdout.write('Connection Error')

    return time, openc, highc, lowc, closec


def getTickers():
    urlCoinGecko = "https://api.coingecko.com/api/v3/coins/list"

    jsonCoinGecko = requests.get(urlCoinGecko)
    jsonCoinGeckoDecoded = json.loads(jsonCoinGecko.content.decode("utf-8"))
    if 'status' in jsonCoinGeckoDecoded:
        print("APIs not working properly:")
        print(jsonCoinGeckoDecoded["status"]["error_message"])
        exit()

    tickersCoinGecko = []
    for item in jsonCoinGeckoDecoded:
        tickersCoinGecko.append(item['id'])

    return tickersCoinGecko
