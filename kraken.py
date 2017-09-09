# coding: utf8
import requests
import sys
import json
import locale
locale.setlocale(locale.LC_ALL, 'de_DE.UTF-8')


def getUrl(x, z):
    return str("https://api.kraken.com/0/public/Ticker?pair=" + makePair(x, z))


def makeResultPair(x, z):
    return str('X' + x + 'Z' + z)


def makePair(x, z):
    return str(x + z)


def getResponse(x, z):
    try:
        current_url = getUrl(x, z)
        # print currentUrl
        data = requests.get(current_url).json()
        # print data
        symbol = makeResultPair(x, z)
        # print symbol
        price_str = data['result']['%s' % symbol]['c'][0]
        return price_str
    except:
        # print "Unexpected error:", sys.exc_info()[0]
        pass   

def formatPrice(unformatted_price, coin_symbol):
    price = locale.currency(float(unformatted_price), symbol=False)
    return str(coin_symbol + " " + price + " €")


def getAllPrices(all_pairs):
    for (crypto_currency, fiat_currency, coin_symbol) in all_pairs:
        try:
            price_str = getResponse(crypto_currency, fiat_currency)
            print formatPrice(price_str, coin_symbol)
        except: 
            pass

def run():
    list_of_tuples = [['ETH', 'EUR', '𝚵'], ['XMR', 'EUR', 'Ⓜ'], ['ZEC', 'EUR', 'ⓩ'], ['LTC', 'EUR', 'Ł'], ['BCH', 'EUR', '฿'], ['XBT', 'EUR', '₿']]
    getAllPrices(list_of_tuples)

run()
