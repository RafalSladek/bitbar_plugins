#!/usr/bin/python
# coding: utf8
import requests
import sys
import json
import locale
locale.setlocale(locale.LC_ALL, 'de_DE.UTF-8')


# <pair_name> = pair name
# a = ask array(<price>, <whole lot volume>, <lot volume>),
# b = bid array(<price>, <whole lot volume>, <lot volume>),
# c = last trade closed array(<price>, <lot volume>),
# v = volume array(<today>, <last 24 hours>),
# p = volume weighted average price array(<today>, <last 24 hours>),
# t = number of trades array(<today>, <last 24 hours>),
# l = low array(<today>, <last 24 hours>),
# h = high array(<today>, <last 24 hours>),
# o = today's opening price

def getUrl(parameters):
    return str("https://api.kraken.com/0/public/Ticker?pair=" + parameters)


def getParameters(all_pairs):
    l = []
    for (crypto_currency, fiat_currency, coin_symbol) in all_pairs:
        l.append(str(makePair(crypto_currency, fiat_currency)))

    return ','.join(l)


def makeResultPair(x, z):
    if (x == 'BCH'):
        return str(x + z)
    else:
        return str('X' + x + 'Z' + z)


def makePair(x, z):
    return str(x + z)


def getResponse(all_pairs):
    current_url = getUrl(getParameters(all_pairs))
    # print current_url
    data = requests.get(current_url).json()
    result = []
    for (crypto_currency, fiat_currency, coin_symbol) in all_pairs:
       # print data
        symbol = makeResultPair(crypto_currency, fiat_currency)
        # print symbol
        result.append(formatPrice(
            data['result']['%s' % symbol]['c'][0], coin_symbol))
    return result


def formatPrice(unformatted_price, coin_symbol):
    price = locale.currency(float(unformatted_price),
                            symbol=False, grouping=True)
    return str(coin_symbol + " " + price + " €")


def formatToBitBar(output):
    return str(output)


def getAllPrices(all_pairs):
    result = getResponse(all_pairs)
    for price in result:
        print formatToBitBar(price)


def run():
    list_of_tuples = [['ETH', 'EUR', '𝚵'], ['XMR', 'EUR', 'Ⓜ'], ['ZEC', 'EUR', 'ⓩ'], [
        'LTC', 'EUR', 'Ł'], ['BCH', 'EUR', '฿'], ['XBT', 'EUR', '₿']]
    getAllPrices(list_of_tuples)


run()
